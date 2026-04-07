from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import requests

@dag(
    dag_id='mini_projeto_cotacao_v1',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['projeto', 'cotacao']
)
def pipeline_cotacao():

    @task()
    def extrair_cotacao():
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()['USDBRL']

    @task()
    def transformar_dados(dados_brutos: dict):
        return {
            "moeda": dados_brutos['code'],
            "valor_bid": float(dados_brutos['bid']),
            "data_cotacao": dados_brutos['create_date']
        }

    @task()
    def carregar_no_postgres(dados: dict):
        pg_hook = PostgresHook(postgres_conn_id='postgres_default')
        insert_sql = """
            INSERT INTO staging_cotacoes (moeda, valor, data_cotacao, processado_em)
            VALUES (%s, %s, %s, NOW())
        """
        pg_hook.run(insert_sql, parameters=(dados['moeda'], dados['valor_bid'], dados['data_cotacao']))

    # Definindo o fluxo (TaskFlow)
    raw_data = extrair_cotacao()
    clean_data = transformar_dados(raw_data)
    carregar_no_postgres(clean_data)

pipeline_cotacao_dag = pipeline_cotacao()