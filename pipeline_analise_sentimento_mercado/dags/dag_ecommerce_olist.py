from datetime import datetime, timedelta
import os
import sys

from airflow.decorators import dag, task

# Adiciona o diretório raiz ao path para que o Airflow encontre a pasta /src
sys.path.insert(0, '/opt/airflow/src')

# Importando as funções que você já criou e testou manualmente
from extract import extract_data
from transform import transform_data
from load import load_data

# configurações paradrão da DAG
default_args = {
  'owner': 'airflow',
  'depends_on_past': False,
  'email_failure_notification': False,
  'retries': 1,
  'retry_delay': timedelta(minutes=5),
}

@dag(
  dag_id='etl_ecommerce_olist_v7',
  default_args=default_args,
  description='Pipeline ETL Intermediário usando Pandas e Postgres',
  schedule='0 */1 * * * ',
  start_date=datetime(2026, 2, 23),
  catchup=False,
  tags=['pessoal', 'pandas', 'ecommerce'],
)
def ecommerce_etl():
  
    @task()
    def extract_task():
      """Extrai os dados brutos para Parquet"""
      #Processamos os dois arquivos baixados
      extract_data("olist_orders_dataset.csv", "orders")
      extract_data("olist_order_items_dataset.csv", "order_item")
      return "Extração concluída"

    @task()
    def transform_task(extract_msg):
      """Aplica as regras de negócio e joins"""
      print(extract_msg)
      transform_data()
      return "Transformação conluída"

    @task()
    def load_task(df_processado):
      """Carrega os dados finais no Postgres"""
      load_data(table_name='fact_orders', df=df_processado)
      return "Carga concluída"

    # Definindo a ordem de execução
    dados_extraidos = extract_task()
    dados_transformados = transform_task(dados_extraidos)
    load_task(dados_transformados)

    # Outra forma de representar a ordem de execução
    # extract_task() >> transform_data(status_extract) >> load_task(status_transform)

# Intancia a DAG
ecommerce_pipeline = ecommerce_etl()
