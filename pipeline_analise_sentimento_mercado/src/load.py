import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote_plus

GOLD_PATH = "data/gold/fact_orders.parquet"
ENV_PATH = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(ENV_PATH)

def get_engine():
  user = os.getenv('user')
  password = os.getenv('password')
  database = os.getenv('database')
  # host = 'host.docker.internal'
  # host = 'localhost' # quando for rodar o codigo pelo terminal
  host = 'postgres' # quando for rodar pela DAG

  # Formato: postgresql://usuario:senha@host:porta/banco
  conn_string = f"postgresql://{user}:{quote_plus(password)}@{host}:5432/{database}"

  print("--- Conectando ao Postgres e Iniciando Carga ---")
  return create_engine(conn_string)

def load_data(table_name:str, df):
  # A leitura acontece APENAS quando a Task for executada
  print(f"--- Lendo dados da Gold: {GOLD_PATH} ---")
  df = pd.read_parquet(GOLD_PATH)
  
  engine = get_engine()

  df.to_sql(
      name=table_name, 
      con=engine, 
      if_exists='replace', 
      index=False,
      chunksize=1000, # Envia em pedaços para não sobrecarregar a rede/memória
      method='multi'  # Método mais rápido para inserção múltipla
  )

  count = pd.read_sql(f'SELECT COUNT(*) FROM {table_name}', con=engine).iloc[0, 0]
  print(f"Total de registros na tabela: {count}")
  return

# Essa linha para baixo será comentada quando criar a pipeline
# load_data('fact_orders', df)