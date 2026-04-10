from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import os

# Função de Callback para Alertas (Simulando envio para Slack/Teams/E-mail)
def on_failure_callback(context):
    exception = context.get('exception')
    dag_id = context.get('dag_run').dag_id
    task_id = context.get('task_instance').task_id
    print(f"🚨 ALERTA DE FALHA: A Task {task_id} na DAG {dag_id} falhou! Erro: {exception}")

@dag(
    dag_id='vortex_analytics_v4_reactive',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={
        'on_failure_callback': on_failure_callback, # Alerta em nível de DAG
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
    },
    tags=['v4', 'sensors', 'callbacks', 'production_ready']
)
def pipeline_v4():

    # 1. SENSOR: Espera um arquivo aparecer no diretório (configurado no Airflow Connection)
    # No Docker, Nesse projeto eu simulei a entrada de um arquivo na pasta /opt/airflow/dags para 
    # testar o sensor de arquivo
    # Crei uma conexão em Admin -> Connections - opção File (path) e na opção extra incluindo
    # o caminho (/opt/airflow/dags)
    esperar_arquivo_sinal = FileSensor(
        task_id='esperar_arquivo_processamento',
        filepath='sinal_processar.txt',
        fs_conn_id='fs_default',
        poke_interval=30, # Checa a cada 30 segundos
        timeout=600,      # Desiste após 10 minutos
        mode='reschedule' # LIBERA O WORKER enquanto espera
    )

    @task
    def processamento_principal():
        print("Arquivo detectado! Iniciando processamento de alta prioridade...")
        return "Sucesso"

    # 2. TRIGGER: Ao final desta DAG, ela dispara automaticamente outra DAG (ex: de limpeza ou BI)
    disparar_dag_bi = TriggerDagRunOperator(
        task_id='trigger_dashboard_update',
        trigger_dag_id='vortex_analytics_v3_dynamic', # Chamando a versão anterior como exemplo
        wait_for_completion=False
    )

    # Fluxo
    esperar_arquivo_sinal >> processamento_principal() >> disparar_dag_bi

pipeline_v4()