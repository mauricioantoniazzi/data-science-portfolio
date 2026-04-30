from airflow.decorators import dag
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
import sys
import os

# 1. Configuração de ambiente para garantir que o Python encontre a v3 no Docker/WSL2
DAGS_FOLDER = "/opt/airflow/dags"
if DAGS_FOLDER not in sys.path:
    sys.path.append(DAGS_FOLDER)

# 2. Importação das funções lógicas refatoradas da v3
try:
    from dag_cotacao_v3_1 import criar_tabela_db, extrair_cotacao_api, carregar_dados_postgres
except ImportError as e:
    raise ImportError(f"Erro ao importar lógica da v3. Verifique se o arquivo dag_cotacao_v3.py está na pasta dags. Erro: {e}")

# 3. Definição de caminhos para o dbt
DBT_PROJECT_DIR = "/opt/airflow/dbt_project"

def pipeline_v3_consolidado():
    """
    Orquestra a lógica de extração e carga da v3 de forma sequencial
    para garantir que os dados cheguem ao Postgres antes do dbt.
    """
    print("--- [ETAPA 1/3] Criando/Verificando tabela no Postgres ---")
    criar_tabela_db()
    
    print("--- [ETAPA 2/3] Extraindo cotações da API ---")
    moedas = ['USD', 'EUR', 'BTC', 'GBP', 'ARS']
    dados_extraidos = []
    
    for moeda in moedas:
        try:
            dado = extrair_cotacao_api(moeda)
            dados_extraidos.append(dado)
            print(f"Sucesso: {moeda}")
        except Exception as err:
            print(f"Erro ao extrair {moeda}: {err}")
    
    print("--- [ETAPA 3/3] Carregando dados no banco ---")
    if dados_extraidos:
        carregar_dados_postgres(dados_extraidos)
        print(f"Carga finalizada com {len(dados_extraidos)} registros.")
    else:
        raise ValueError("Falha crítica: Nenhum dado foi extraído da API.")

@dag(
    dag_id='vortex_analytics_full_pipeline',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['v5', 'final_project', 'dbt', 'full_pipeline']
)
def vortex_analytics_v5():

    # TASK 1: O "E" e o "L" do ETL (Extração e Carga)
    extract_and_load = PythonOperator(
        task_id='extract_and_load_api',
        python_callable=pipeline_v3_consolidado,
        do_xcom_push=False
    )

    # TASK 2: O "T" do ETL (Transformação com dbt)
    # Rodamos o dbt run apontando para o diretório e profile corretos
    dbt_transformation = BashOperator(
        task_id='dbt_transformation',
        bash_command=(
            f'dbt run --project-dir {DBT_PROJECT_DIR} '
            f'--profiles-dir {DBT_PROJECT_DIR}'
        )
    )

    # Definindo a dependência: dbt só roda se a carga no banco der certo
    extract_and_load >> dbt_transformation

# Instanciação da DAG
vortex_analytics_v5()