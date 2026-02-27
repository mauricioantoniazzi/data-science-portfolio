import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine, text
import re
from urllib.parse import quote_plus
import os
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(ENV_PATH)

def clean_phone(phone):
  """Remove tudo que não é numero e garante o formato DDI+DDD+Número"""
  if not phone: return None
  digits = re.sub(r'\D', '', str(phone))
  # Se não tem DDI (55), adiciona
  if len(digits) == 11 and not digits.startswith('55'):
      digits = '55' + digits

  return digits

def calculate_score(email, origem):
  """ Lógica Simples de Lead Score: Corporativo vale mais que Gmail/Hotmail """
  score = 10
  email = str(email).lower()
  public_domains = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com']

  if any(domain in email for domain in public_domains):
    score = 5

  # Bônus por orgiem premium
  if origem.lower() in ['linkedin', 'google_ads']:
    score += 5

  return score

def run_pipeline():
  print("Iniciando Pipeline de Leads...")

  # 1. Configuração Google Sheets
  scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
  # Caminho para o JSON dentro do container
  json_path = "/opt/airflow/config/google_key.json"
    
  creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
  client = gspread.authorize(creds)
  sheet = client.open("Leads_Landing_Page").sheet1
  df = pd.DataFrame(sheet.get_all_records())

  if df.empty:
     print("Planilha vazia.")
     return
  
  # ADICIONE ESTA LINHA AQUI:
  df = df.drop_duplicates(subset=['email'], keep='first')
  
  # 2. Transformação (Pandas)
  print("Limpando e Transformando dados...")
  df['telefone'] = df['telefone'].apply(clean_phone)
  df['lead_score'] = df.apply(lambda x: calculate_score(x['email'], x['origem']), axis=1)
  df['processed_at'] = pd.Timestamp.now()

  # 3. Conexão Postgres
  user = os.getenv('user')
  password = os.getenv('password')
  database = os.getenv('database')
  # host = 'host.docker.internal'
  # host = 'localhost' # quando for rodar o codigo pelo terminal
  host = 'postgres' # quando for rodar pela DAG

  engine = create_engine(f'postgresql://{user}:{quote_plus(password)}@{host}:5432/{database}')

  # 4. Lógica de UPSERT (O coração da Engenharia)
  # Vamos inserir linha a linha para garantir o 'ON CONFLICT' do Postgres
  with engine.begin() as conn:
    for _, row in df.iterrows():
        upsert_query = text("""
            INSERT INTO silver_leads (id_original, nome, email, telefone, origem, data_criacao, lead_score)
            VALUES (:id_orig, :nome, :email, :tel, :origem, :dt_cria, :score)
            ON CONFLICT (email) 
            DO UPDATE SET 
                nome = EXCLUDED.nome,
                telefone = EXCLUDED.telefone,
                lead_score = EXCLUDED.lead_score,
                processed_at = CURRENT_TIMESTAMP;
        """)
        
        conn.execute(upsert_query, {
            "id_orig": row['id_original'],
            "nome": row['nome'],
            "email": row['email'],
            "tel": row['telefone'],
            "origem": row['origem'],
            "dt_cria": pd.to_datetime(row['data_criacao']) if 'data_criacao' in row and row['data_criacao'] != "" else pd.Timestamp.now(),
            "score": row['lead_score']
        })
            
    print(f"✅ Sucesso! {len(df)} leads processados/atualizados na Silver.")

if __name__ == "__main__":
  run_pipeline()