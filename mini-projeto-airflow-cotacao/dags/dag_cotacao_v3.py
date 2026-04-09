from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import requests

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
    """
    Simula a leitura de um arquivo YAML, banco de dados ou variável.
    Se amanhã você adicionar 'BCT' ou 'GBP' aqui, a DAG cria as tasks sozinha
    """
    return ['USD', 'EUR', 'BTC', 'GBP', 'ARS']
  
  @task
  def criar_tabela():
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    pg_hook.run("""
      CREATE TABLE IF NOT EXISTS staging_cotacoes(
                moeda VARCHAR(10),
                valor DECIMAL(10,4),
                data_cotacao TIMESTAMP,
                processado_em TIMESTAMP
                );
                """)
    
  @task
  def extrair_moeda(moeda: str):
    # A lógica permanece limpa, o Airflow cuida da paralelização
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url).json()
    data = response[f"{moeda}BRL"]
    return {
      "moeda": moeda,
      "valor": float(data['bid']),
      "data": data['create_date'],
      "data_proc": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
  
  @task
  def carregar_no_postgres(dados:list):
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    insert_query = """
      INSERT INTO staging_cotacoes (moeda, valor, data_cotacao, processado_em)
      VALUES (%s, %s, %s, %s)
    """
    for item in dados:
      pg_hook.run(insert_query, parameters=(
        item['moeda'], item['valor'], item['data'], item['data_proc']
      ))

  # --- FLUXO DINÂMICO ---
  setup_db = criar_tabela()
  moedas = obter_lista_configuracao()
  
  #A MÁGICA: .expand criar uma task para cada item da lista 'moedas'
  extracao_dinamica = extrair_moeda.expand(moeda=moedas)

  setup_db >> extracao_dinamica >> carregar_no_postgres(extracao_dinamica)

pipeline_v3() 