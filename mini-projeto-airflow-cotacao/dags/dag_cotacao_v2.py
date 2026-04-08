from airflow.decorators import dag, task, task_group
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import requests

@dag(
    dag_id='vortex_analytics_v2',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['v2', 'task_groups', 'xcom']
)
def pipeline_v2():

    @task
    def criar_tabela():
        pg_hook = PostgresHook(postgres_conn_id='postgres_default')
        query = """
            CREATE TABLE IF NOT EXISTS staging_cotacoes (
                moeda VARCHAR(10),
                valor_bid DECIMAL(10, 4),
                data_cotacao TIMESTAMP,
                data_processamento TIMESTAMP
            );
        """
        pg_hook.run(query)

    @task_group(group_id='extracao_multicanal')
    def extracao():
        
        @task
        def extrair_moeda(moeda: str):
            url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
            response = requests.get(url).json()
            data = response[f"{moeda}BRL"]
            # O retorno vai automaticamente para o XCom
            return {
                "moeda": moeda,
                "valor": float(data['bid']),
                "data": data['create_date']
            }

        # Criamos tasks paralelas dentro do grupo
        task_usd = extrair_moeda('USD')
        task_eur = extrair_moeda('EUR')
        
        return [task_usd, task_eur]

    @task
    def consolidar_dados(dados_extraidos: list):
        """
        Esta task recebe os dados via XCom. 
        Note que 'dados_extraidos' é uma lista com os retornos das tasks do grupo.
        """
        print(f"Consolidando {len(dados_extraidos)} registros...")
        # Adicionamos um timestamp de processamento
        for item in dados_extraidos:
            item['data_proc'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return dados_extraidos

    @task
    def carregar_no_postgres(dados_finalizados: list):
        pg_hook = PostgresHook(postgres_conn_id='postgres_default')
        
        insert_query = """
            INSERT INTO staging_cotacoes (moeda, valor, data_cotacao, processado_em)
            VALUES (%s, %s, %s, %s)
        """
        
        for item in dados_finalizados:
            pg_hook.run(insert_query, parameters=(
                item['moeda'], 
                item['valor'], 
                item['data'], 
                item['data_proc']
            ))

    # Definindo a Orquestração
    tabela = criar_tabela()
    dados_brutos = extracao()
    dados_limpos = consolidar_dados(dados_brutos)
    
    tabela >> dados_brutos >> dados_limpos >> carregar_no_postgres(dados_limpos)

pipeline_v2()