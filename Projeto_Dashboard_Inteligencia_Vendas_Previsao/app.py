import streamlit as st

# Importações de Dados e Configuração
from modules.core.db_connector import load_data
from modules.core.config import PAGE_CONFIG, CUSTOM_CSS, DIMENSIONS_TREEMAP
from modules.services.page_filters import (
    setup_item1_filters,
    setup_item2_filters,
    setup_item3_filters,
    setup_item4_filters
)

# Importações de Páginas
from modules.pages.principais_indicadores import render_principais_indicadores
from modules.pages.decomposicao_arvore_hierarquica import render_decomposicao_arvore_hierarquica
from modules.pages.decomposicao_dinamica import render_decomposicao_dinamica
from modules.pages.previsao_vendas import render_previsao_vendas

# ==============================================================================
# CONFIGURAÇÃO INICIAL DO STREAMLIT
# ==============================================================================

st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==============================================================================
# 1. CARREGAMENTO DE DADOS
# ==============================================================================

df_vendas = load_data()

if df_vendas.empty:
    st.error("Não foi possível carregar os dados. Verifique a conexão com o SQL Server.")
    st.stop()

# Preparar coluna Data para Prophet
df_vendas['Data'] = df_vendas['Data_Venda']

# ==============================================================================
# 2. MENU DE NAVEGAÇÃO
# ==============================================================================

with st.sidebar:
    st.title("Menu de Navegação")
    menu_selection = st.radio(
        "Selecione o Item",
        [
            "Principais Indicadores",
            "Decomposição (Árvore Hierárquica)",
            "Decomposição Dinâmica (Treemap)",
            "Previsão (Forecasting)"
        ],
        key="menu_radio"
    )

# ==============================================================================
# 3. LÓGICA PARA CADA ITEM DO MENU
# ==============================================================================

if menu_selection == "Principais Indicadores":
    st.header("Principais Indicadores e Análise Temporal")
    
    # Configurar filtros
    filters = setup_item1_filters(df_vendas)
    
    # Renderizar página
    render_principais_indicadores(df_vendas, filters)

elif menu_selection == "Decomposição (Árvore Hierárquica)":
    
    # Configurar filtros
    filters = setup_item2_filters(df_vendas)
    
    # Renderizar página
    render_decomposicao_arvore_hierarquica(df_vendas, filters)

elif menu_selection == "Decomposição Dinâmica (Treemap)":
    
    # Configurar filtros
    filters = setup_item3_filters(df_vendas)
    
    # Filtrar dados conforme seleção
    df_vendas_filtered = df_vendas[
        (df_vendas['Ano'].isin(filters['years']))
        & (df_vendas['Categoria'].isin(filters['categories']) if filters['categories'] else True)
        & (df_vendas['Mes'].isin(filters['months']) if filters['months'] else True)
    ].copy()
    
    # Renderizar página
    render_decomposicao_dinamica(df_vendas_filtered, filters, DIMENSIONS_TREEMAP)

elif menu_selection == "Previsão (Forecasting)":
    
    # Configurar filtros
    filters = setup_item4_filters(df_vendas)
    
    # Renderizar página
    render_previsao_vendas(df_vendas, filters)