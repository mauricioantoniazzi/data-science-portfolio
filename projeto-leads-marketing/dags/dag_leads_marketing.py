from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime, timedelta
import sys
import os
import json

# Adiciona o caminho /opt/airflow/src ao Python Path para o Airflow achar o script
sys.path.insert(0, '/opt/airflow/src')

# Importa a função principal do seu script de processamento
try:
  from process_leads import run_pipeline
except ImportError:
  def run_pipeline():
    import subprocess
    subprocess.run(["python2", "/opt/airflow/src/process_leads.py"], check=True)

# Configurações básicas da DAG
default_args = {
  'owner': 'engenharia_dados',
  'depends_on_past': False,
  'start_date': datetime(2026, 2, 25),
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(minutes=5),
}

with DAG(
  'pipeline_leads_sheets_to_postgres_v2',
  default_args=default_args,
  description='Extração de sheets com Upsert no Postgres',
  schedule='0 8 * * * ',
  catchup=False,
  tags=['marketing', 'leads'],
) as dag:
  
  # Task única que executa todo o processo de Ingestão e Transformação
  task_processar_leads = PythonOperator(
    task_id='ingestao_e_transformacao_leads',
    python_callable=run_pipeline
  )

  task_notificar_n8n = HttpOperator(
      task_id='notificar_n8n',
      http_conn_id='n8n_webhook', # Vamos criar essa conexão no Airflow
      endpoint='webhook-test/airflow-leads-trigger', # O final da URL do seu Webhook
      method='POST',
      data=json.dumps({"status": "sucesso", "projeto": "leads_marketing"}),
      headers={"Content-Type": "application/json"},
  )

  task_processar_leads >> task_notificar_n8n
