# ==============================================================================
# LÓGICA DE FILTROS POR PÁGINA
# ==============================================================================
# Este arquivo centraliza a lógica de criação de filtros para cada página

import streamlit as st
from modules.db_connector import get_distinct_values
from modules.config import MEDIDAS_KPI


def setup_item1_filters(df):
    """
    Configura os filtros para o Item 1: Principais Indicadores
    Retorna um dicionário com todos os filtros selecionados
    """
    
    # Obter valores distintos
    available_years = get_distinct_values(df, 'Ano')
    available_months = get_distinct_values(df, 'Mes')
    available_brands = get_distinct_values(df, 'Marca')
    available_categories = get_distinct_values(df, 'Categoria')
    available_subcategories = get_distinct_values(df, 'Subcategoria')
    available_products = get_distinct_values(df, 'Descricao_Produto')
    
    with st.sidebar:
        st.subheader("Filtros de Análise")
        
        selected_measure = st.selectbox(
            "Medida Principal (KPI Variável):",
            options=MEDIDAS_KPI,
            index=2,
            key="filter_medida"
        )

        selected_year = st.selectbox(
            "Ano Selecionado:",
            options=available_years,
            index=len(available_years) - 2 if len(available_years) > 1 else 0,
            key="filter_ano"
        )
        
        selected_months = st.multiselect(
            "Mês(es) Selecionado(s):",
            options=available_months,
            default=available_months,
            key="filter_mes"
        )
        
        st.write("---")
        selected_brands = st.multiselect("Marca:", available_brands, key="filter_marca")
        selected_categories = st.multiselect("Categoria:", available_categories, key="filter_categoria")
        selected_subcategories = st.multiselect("Subcategoria:", available_subcategories, key="filter_subcategoria")
        selected_products = st.multiselect("Produto:", available_products, key="filter_produto")

    return {
        'measure': selected_measure,
        'year': selected_year,
        'months': selected_months,
        'brands': selected_brands,
        'categories': selected_categories,
        'subcategories': selected_subcategories,
        'products': selected_products
    }


def setup_item2_filters(df):
    """
    Configura os filtros para o Item 2: Decomposição (Árvore Hierárquica)
    Retorna um dicionário com os filtros selecionados
    """
    available_years = get_distinct_values(df, 'Ano')
    
    with st.sidebar:
        st.subheader("Filtro para Decomposição")
        
        selected_measure = st.selectbox(
            "Medida para Decomposição:",
            options=MEDIDAS_KPI,
            index=2,
            key="filter_medida_decomp"
        )
        
        selected_year = st.selectbox(
            "Ano Inicial:",
            options=available_years,
            index=len(available_years) - 2 if len(available_years) > 1 else 0,
            key="filter_ano_decomp"
        )

    return {
        'measure': selected_measure,
        'year': selected_year
    }


def setup_item3_filters(df):
    """
    Configura os filtros para o Item 3: Decomposição Dinâmica (Treemap)
    Retorna um dicionário com os filtros selecionados
    """
    available_years = sorted(df['Ano'].unique(), reverse=False)
    available_months = get_distinct_values(df, 'Mes')
    available_categories = get_distinct_values(df, 'Categoria')
    
    with st.sidebar:
        st.subheader("Filtro para Decomposição")
        
        selected_measure = st.selectbox(
            "Medida para Decomposição:",
            options=MEDIDAS_KPI,
            index=2,
            key="filter_medida_decomp"
        )
        
        selected_years = st.sidebar.multiselect(
            'Anos Selecionados (para Comparação):',
            options=available_years,
            default=available_years[-2:]
        )

        selected_months = st.multiselect(
            "Mês(es) Selecionado(s):",
            options=available_months,
            default=available_months,
            key="filter_mes"
        )

        selected_categories = st.multiselect(
            "Categoria:", 
            available_categories, 
            key="filter_categoria"
        )

    return {
        'measure': selected_measure,
        'years': selected_years,
        'months': selected_months,
        'categories': selected_categories
    }


def setup_item4_filters(df):
    """
    Configura os filtros para o Item 4: Previsão (Forecasting)
    Retorna um dicionário com os filtros selecionados
    """
    with st.sidebar:
        st.subheader("Filtro para Previsão")
        
        selected_measure = st.selectbox(
            "Medida para Previsão",
            options=MEDIDAS_KPI,
            index=2,
            key="filter_medida_prev"
        )

    return {
        'measure': selected_measure
    }
