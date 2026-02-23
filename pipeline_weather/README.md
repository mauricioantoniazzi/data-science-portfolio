# Ativar arquivo .env
source .venv/bin/activate

# Instalando dependencias
 uv add python-dotenv
 uv add requests
 uv add pandas
 uv add pandas
 uv add sqlalchemy
 uv add psycopg2-binary
  

# rodar a aplicação em um arquivo específico
uv run src/extract_data.py