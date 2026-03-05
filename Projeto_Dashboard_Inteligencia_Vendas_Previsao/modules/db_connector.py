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
    query = """
    SELECT
        V.ID_Pedido,
        V.Data_Venda,
        V.Data_Entrega,
        V.Qtde,
        V.Valor_Total,
        P.Descricao_Produto,
        P.Custo,
        P.Preco_Unitario,
        P.Tributos,
        M.Marca,
        C.Categoria,
        SC.Subcategoria,
        CL.Nome AS Nome_Cliente,
        CL.Genero,
        CD.Cidade,
        CD.UF,
        CA.Descricao_Canal
    FROM 
        Venda V
    JOIN Produto P ON V.ID_Produto = P.ID_Produto
    JOIN Marca M ON P.ID_Marca = M.ID_Marca
    JOIN Subcategoria SC ON P.ID_Subcategoria = SC.ID_Subcategoria
    JOIN Categoria C ON SC.ID_Categoria = C.ID_Categoria
    JOIN Cliente CL ON V.ID_Cliente = CL.ID_Cliente
    JOIN Cidade CD ON CL.ID_Cidade = CD.ID_Cidade
    JOIN Canal CA ON V.ID_Canal = CA.ID_Canal
    ORDER BY 
        V.Data_Venda;
    """
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

if __name__ == '__main__':
    # Teste de conexão (executado apenas se o script for rodado diretamente)
    print("Testando conexão e carregamento de dados...")
    df = load_data()
    if not df.empty:
        print("Dados carregados com sucesso! Primeiras 5 linhas:")
        print(df.head())
    else:
        print("Falha ao carregar os dados.")