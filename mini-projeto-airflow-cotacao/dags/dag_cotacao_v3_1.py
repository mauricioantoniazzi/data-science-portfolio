from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import requests

# --- FUNÇÕES LÓGICAS (ACESSÍVEIS PARA IMPORTAÇÃO NA V5) ---

def criar_tabela_db():
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    pg_hook.run("""
        CREATE TABLE IF NOT EXISTS staging_cotacoes(
            moeda VARCHAR(10),
            valor DECIMAL(10,4),
            data_cotacao TIMESTAMP,
            processado_em TIMESTAMP
        );
    """)

def extrair_cotacao_api(moeda: str):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url).json()
    data = response[f"{moeda}BRL"]
    return {
        "moeda": moeda,
        "valor": float(data['bid']),
        "data": data['create_date'],
        "data_proc": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

def carregar_dados_postgres(dados: list):
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    insert_query = """
        INSERT INTO staging_cotacoes (moeda, valor, data_cotacao, processado_em)
        VALUES (%s, %s, %s, %s)
    """
    for item in dados:
        pg_hook.run(insert_query, parameters=(
            item['moeda'], item['valor'], item['data'], item['data_proc']
        ))

# --- DEFINIÇÃO DA DAG ---

@dag(
    dag_id='vortex_analytics_v3_dynamic',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['v3', 'dynamic_mapping', 'scalability']
)
def pipeline_v3():

    @task
    def obter_lista_configuracao():
        return ['USD', 'EUR', 'BTC', 'GBP', 'ARS']
  
    @task
    def criar_tabela_task():
        criar_tabela_db()
    
    @task
    def extrair_moeda_task(moeda: str):
        return extrair_cotacao_api(moeda)
  
    @task
    def carregar_no_postgres_task(dados: list):
        carregar_dados_postgres(dados)

    # Fluxo
    setup_db = criar_tabela_task()
    moedas = obter_lista_configuracao()
    extracao_dinamica = extrair_moeda_task.expand(moeda=moedas)

    setup_db >> extracao_dinamica >> carregar_no_postgres_task(extracao_dinamica)

pipeline_v3()