# ==============================================================================
# ITEM 2: DECOMPOSIÇÃO (ÁRVORE HIERÁRQUICA)
# ==============================================================================

import streamlit as st
import plotly.express as px


def render_decomposicao_arvore_hierarquica(df, filters):
    """
    Decomposição em Árvore Hierárquica
    
    Args:
        df: DataFrame completo de vendas
        filters: Dicionário com os filtros selecionados
    """
    
    selected_year = filters['year']
    selected_measure = filters['measure']
    
    st.header(f"Decomposição (Árvore Hierárquica) | Ano: {selected_year}")
    
    # Filtrar apenas o ano selecionado
    df_tree = df[df['Ano'] == selected_year].copy()
    
    # Criar o Treemap
    fig = px.treemap(
        df_tree,
        path=['Categoria', 'Subcategoria', 'Descricao_Produto'],
        values=selected_measure,
        color='Categoria',
        title=f'Decomposição Hierárquica de {selected_measure} por Categoria/Subcategoria/Produto ({selected_year})',
        color_discrete_sequence=px.colors.qualitative.Prism,
    )
    
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25)
    )
    
    fig.update_traces(
        hovertemplate='%{label}<br>Valor: %{value:,.2f}<extra></extra>'
    )
    
    st.plotly_chart(fig, use_container_width=True)
