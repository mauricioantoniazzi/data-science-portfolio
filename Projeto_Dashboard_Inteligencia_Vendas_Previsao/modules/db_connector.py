import pyodbc
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do caminho específico
load_dotenv("config/.env")

# Configurações de conexão (ajuste conforme seu ambiente)
# Usando o cache do Streamlit para evitar reconexões desnecessárias
@st.cache_resource
def get_db_connection():
    """Cria e retorna a conexão com o SQL Server."""
    try:
        # Recupera os dados do arquivo .env
        driver = os.getenv('DB_DRIVER')
        server = os.getenv('DB_SERVER')
        database = os.getenv('DB_NAME')

        conn_str = (
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            'Trusted_Connection=yes;' # Geralmente necessário para conexões locais/Windows
        )

        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para carregar o DataFrame principal
@st.cache_data(ttl=600)  # Cache de 10 minutos para os dados
def load_data():
    """Carrega todos os dados necessários em um único DataFrame."""
    conn = get_db_connection()
    if conn is None:
        return pd.DataFrame()

    # Consulta SQL que faz o JOIN de todas as tabelas necessárias
    # Adaptar esta consulta conforme a necessidade exata de colunas
    query = "SELECT * FROM dbo.fct_vendas_indicadores ORDER BY Data_Venda"
    try:
        df = pd.read_sql(query, conn)
        # Adicionar colunas de Ano, Mês e Métricas de Negócio (Desconto, Receita Líquida, Margem)
        
        # 1. Ajuste de Tipos
        df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
        
        # 2. Criação de Colunas de Tempo
        df['Ano'] = df['Data_Venda'].dt.year
        df['Mes'] = df['Data_Venda'].dt.month
        df['Nome_Mes'] = df['Data_Venda'].dt.strftime('%B') # Nome do mês

        # 3. Criação de Métricas de Negócio (Assumindo Desconto = 10% do Valor_Total para simulação, 

        # Faturamento Bruto (Valor Total da Venda)
        df['Faturamento Bruto'] = df['Qtde'] * df['Preco_Unitario']

        # Tributos Total da Venda
        df['Tributos Total'] = df['Tributos'] * df['Qtde']
        
        # Custo Total da Venda
        df['Custos'] = df['Qtde'] * df['Custo']

        # Quantidade: SUM(Qtde)
        df['Quantidade'] = df['Qtde']

        # Receita Bruta: SUM(Valor Total da Venda)
        df['Receita Bruta'] = df['Valor_Total']

        # Desconto: [Faturamento Bruto] - [Receita Bruta]
        df['Desconto'] = df['Faturamento Bruto'] - df['Receita Bruta']

        # Receita Líquida: [Receita Bruta] - [Tributos]
        df['Receita Líquida'] = df['Receita Bruta'] - df['Tributos Total']

        # Margem: [Receita Líquida] - [Custos]
        df['Margem'] = df['Receita Líquida'] - df['Custos']
        
        return df
    except Exception as e:
        st.error(f"Erro ao executar a consulta: {e}")
        return pd.DataFrame()

# Obter valores distintos para filtros
@st.cache_data(ttl=3600)
def get_distinct_values(df, column_name):
    """Retorna uma lista de valores únicos de uma coluna."""
    if df.empty:
        return []
    return sorted(df[column_name].unique())

def run_query(query):
    """Executa uma consulta SQL genérica e retorna um DataFrame."""
    conn = get_db_connection() # Reutiliza a função de conexão com cache
    if conn is None:
        return pd.DataFrame()
    
    try:
        # Usa o pandas para ler a query diretamente da conexão
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"Erro ao executar a consulta estratégica: {e}")
        return pd.DataFrame()
    
if __name__ == '__main__':
    # Teste de conexão (executado apenas se o script for rodado diretamente)
    print("Testando conexão e carregamento de dados...")
    df = load_data()
    if not df.empty:
        print("Dados carregados com sucesso! Primeiras 5 linhas:")
        print(df.head())
    else:
        print("Falha ao carregar os dados.")