# ==============================================================================
# ITEM 3: DECOMPOSIÇÃO DINÂMICA (TREEMAP)
# ==============================================================================

import streamlit as st
import plotly.express as px


def render_item3(df, filters, dimensions_list):
    """
    Renderiza o Item 3: Decomposição Dinâmica com Treemap Interativo
    
    Args:
        df: DataFrame filtrado de vendas
        filters: Dicionário com os filtros selecionados
        dimensions_list: Lista de dimensões disponíveis para hierarquia
    """
    
    selected_years = filters['years']
    selected_measure = filters['measure']
    
    st.header(f"Item 3: Decomposição Dinâmica (Treemap) | Anos: {', '.join(map(str, selected_years))}")
    st.markdown("---")

    if not selected_years:
        st.warning("Selecione pelo menos um ano para visualizar o Treemap.")
        return

    # -------------------------------------------------------
    # CONTROLE DE ORDEM E PROFUNDIDADE
    # -------------------------------------------------------
    
    selected_path_order = st.multiselect(
        "Selecione a **Ordem** da Hierarquia (Nó 1, Nó 2, ...):",
        options=dimensions_list,
        default=dimensions_list[:3], 
        help="A ordem dos itens selecionados define o caminho de drill-down (Nó 1 -> Nó 2 -> ...)."
    )

    if not selected_path_order:
        st.warning("Selecione pelo menos um nó de hierarquia.")
        return

    plotly_path = selected_path_order
    max_depth = len(selected_path_order)

    if max_depth > 1:
        current_depth = st.slider(
            "Profundidade Máxima de Exibição Inicial:",
            min_value=1,
            max_value=max_depth,
            value=min(3, max_depth),
            help="Define o número máximo de níveis a serem exibidos antes de clicar (Max Depth)."
        )
    else:
        current_depth = 1 
        st.info(f"Profundidade fixa em 1 (Apenas o Nó: **{plotly_path[0]}**).")
        
    st.markdown("---")

    # -------------------------------------------------------
    # RENDERIZAÇÃO EM LOOP POR ANO (Layout de 2 Colunas)
    # -------------------------------------------------------
    
    num_years = len(selected_years)
    
    for i in range(0, num_years, 2):
        
        cols = st.columns(2)
        
        # Primeiro ano (coluna esquerda)
        year1_index = i
        if year1_index < num_years:
            year = selected_years[year1_index]
            
            with cols[0]:
                st.markdown(f"#### 🗓️ Ano: {year}")
                
                df_tree_year = df[df['Ano'] == year].copy()
                if df_tree_year.empty:
                    st.info(f"Sem dados para o ano {year}.")
                else:
                    fig = px.treemap(
                        df_tree_year,
                        path=plotly_path,
                        values=selected_measure,
                        color=plotly_path[0], 
                        maxdepth=current_depth, 
                        color_discrete_sequence=px.colors.qualitative.Prism,
                    )
                    fig.update_layout(
                        title=f'{selected_measure} - {year}', 
                        margin=dict(t=50, l=10, r=10, b=10)
                    )
                    fig.update_traces(
                        textinfo="label+percent entry", 
                        hovertemplate='%{label}<br>Valor: R$ %{value:,.2f}<extra></extra>'
                    )
                    st.plotly_chart(fig, use_container_width=True)

        # Segundo ano (coluna direita)
        year2_index = i + 1
        if year2_index < num_years:
            year = selected_years[year2_index]
            
            with cols[1]:
                st.markdown(f"#### 🗓️ Ano: {year}")
                
                df_tree_year = df[df['Ano'] == year].copy()
                if df_tree_year.empty:
                    st.info(f"Sem dados para o ano {year}.")
                else:
                    fig = px.treemap(
                        df_tree_year,
                        path=plotly_path,
                        values=selected_measure,
                        color=plotly_path[0], 
                        maxdepth=current_depth, 
                        color_discrete_sequence=px.colors.qualitative.Prism,
                    )
                    fig.update_layout(
                        title=f'{selected_measure} - {year}', 
                        margin=dict(t=50, l=10, r=10, b=10)
                    )
                    fig.update_traces(
                        textinfo="label+percent entry", 
                        hovertemplate='%{label}<br>Valor: R$ %{value:,.2f}<extra></extra>'
                    )
                    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
        ---
        **Dicas de Uso:**
        * A ordem de **Drill-Down** é definida pela sua seleção no campo "Selecione a Ordem da Hierarquia".
        * Compare o tamanho dos blocos entre os anos para visualizar a **migração de *market share***.
    """)
