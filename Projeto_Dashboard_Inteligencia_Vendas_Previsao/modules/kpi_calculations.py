import streamlit as st
import numpy as np

@st.cache_data
def apply_filters(df, year, months, brands, categories, subcategories, products):
    """Aplica todos os filtros selecionados ao DataFrame de vendas."""
    df_filtered = df.copy()

    # 1. Filtro de Ano (Obrigatório para o cálculo de YoY)
    df_filtered = df_filtered[df_filtered['Ano'].isin([year, year - 1])]

    # 2. Filtro de Mês
    if months:
        # Nota: O filtro de mês deve ser aplicado APENAS aos meses do ANO ATUAL e ANO ANTERIOR.
        # Caso contrário, o cálculo de YoY será inconsistente.
        df_filtered = df_filtered[df_filtered['Mes'].isin(months)]

    # 3. Filtros Hierárquicos (Aplicar se houver seleção)
    if brands:
        df_filtered = df_filtered[df_filtered['Marca'].isin(brands)]
    if categories:
        df_filtered = df_filtered[df_filtered['Categoria'].isin(categories)]
    if subcategories:
        df_filtered = df_filtered[df_filtered['Subcategoria'].isin(subcategories)]
    if products:
        df_filtered = df_filtered[df_filtered['Descricao_Produto'].isin(products)]

    return df_filtered


def calculate_kpis(df_filtered, target_year, measure):
    """
    Calcula o valor atual, o valor do ano anterior e o YoY para uma métrica específica.
    Margem é tratada como percentual (Margem / Receita Líquida).
    """
    
    # 1. Filtrar o DataFrame para o ano atual e o ano anterior
    df_current_year = df_filtered[df_filtered['Ano'] == target_year]
    df_previous_year = df_filtered[df_filtered['Ano'] == target_year - 1]

    # Inicializa valores
    current_value = 0
    previous_value = 0

    if measure == 'Margem':
        # --- Lógica Específica para MARGEM (%) ---
        # Numerador: Margem (Valor Absoluto)
        current_abs_margem = df_current_year['Margem'].sum()
        previous_abs_margem = df_previous_year['Margem'].sum()

        # Denominador: Receita Líquida
        current_receita_liquida = df_current_year['Receita Líquida'].sum()
        previous_receita_liquida = df_previous_year['Receita Líquida'].sum()
        
        # Margem Percentual
        if current_receita_liquida != 0:
            current_value = (current_abs_margem / current_receita_liquida) * 100
        if previous_receita_liquida != 0:
            previous_value = (previous_abs_margem / previous_receita_liquida) * 100

    elif measure == 'Quantidade':
        # --- Lógica para Quantidade ---
        current_value = df_current_year['Quantidade'].sum()
        previous_value = df_previous_year['Quantidade'].sum()

    else:
        # --- Lógica para Métricas Financeiras Absolutas (R$) ---
        current_value = df_current_year[measure].sum()
        previous_value = df_previous_year[measure].sum()


    # 2. Calcular o YoY (Variação Percentual)
    if previous_value != 0 and not np.isnan(previous_value):
        yoy = ((current_value - previous_value) / previous_value) * 100
    else:
        yoy = 0.0
    
    yoy_rounded = round(yoy, 2) # Arredonda para 2 casas decimais

    # 3. Formatação
    if measure == 'Margem':
        # Formatar como Percentual
        current_value_fmt = f"{current_value:.2f}%"
        previous_value_fmt = f"{previous_value:.2f}%"
    elif measure == 'Quantidade':
        # Formatar como Inteiro
        current_value_fmt = f"{int(current_value):,}".replace(",", ".")
        previous_value_fmt = f"{int(previous_value):,}".replace(",", ".")
    else:
        # Formatar como Moeda (R$)
        current_value_fmt = f"R$ {current_value:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
        previous_value_fmt = f"R$ {previous_value:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
        
    yoy_fmt = f"{yoy:.1f}%"

    return {
        'current_value': current_value_fmt,
        'previous_value': previous_value_fmt,
        'yoy': yoy_fmt,
        'yoy_delta': yoy_rounded # Retorna o valor numérico para a cor do delta
    }