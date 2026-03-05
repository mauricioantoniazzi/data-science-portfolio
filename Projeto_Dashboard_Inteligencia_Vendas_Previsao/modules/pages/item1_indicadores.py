# ==============================================================================
# ITEM 1: PRINCIPAIS INDICADORES
# ==============================================================================

import streamlit as st
import pandas as pd
from modules.kpi_calculations import apply_filters, calculate_kpis
from modules.chart_functions import (
    create_sparkline, 
    create_pie_chart, 
    create_bar_chart, 
    create_line_chart
)


def render_item1(df, filters):
    """
    Renderiza o Item 1: Principais Indicadores
    
    Args:
        df: DataFrame completo de vendas
        filters: Dicionário com os filtros selecionados
    """
    
    selected_year = filters['year']
    selected_measure = filters['measure']
    selected_months = filters['months']
    selected_brands = filters['brands']
    selected_categories = filters['categories']
    selected_subcategories = filters['subcategories']
    selected_products = filters['products']
    
    # Aplicar os filtros para obter os dados
    df_filtered = apply_filters(
        df, selected_year, selected_months, selected_brands, 
        selected_categories, selected_subcategories, selected_products
    )

    # -------------------------------------------------------
    # KPIS (3 COLUNAS: VARIÁVEL, DESCONTO, MARGEM)
    # -------------------------------------------------------
    
    kpi_variable = selected_measure
    kpi_fixed_1 = 'Desconto'
    kpi_fixed_2 = 'Margem'
    
    # Calcular os KPIs
    data_variable = calculate_kpis(df_filtered, selected_year, kpi_variable)
    data_desconto = calculate_kpis(df_filtered, selected_year, kpi_fixed_1)
    data_margem = calculate_kpis(df_filtered, selected_year, kpi_fixed_2)
    
    col1, col2, col3 = st.columns(3)

    # CARD 1: KPI VARIÁVEL
    with col1:
        st.metric(
            label=f"⭐ {kpi_variable} ({selected_year})",
            value=data_variable['current_value'],
            delta=data_variable['yoy_delta'],
            delta_color="normal" if data_variable['yoy_delta'] > 0 else "inverse"
        )
        st.markdown(f"**Ano Ant. ({selected_year - 1}):** {data_variable['previous_value']}")
        st.markdown(f"**YoY:** {data_variable['yoy']}")
        fig_var = create_sparkline(df_filtered, kpi_variable, selected_year, selected_year - 1)
        st.plotly_chart(fig_var, use_container_width=True, config={'displayModeBar': False})

    # CARD 2: DESCONTO
    with col2:
        st.metric(
            label=f"💸 {kpi_fixed_1} ({selected_year})",
            value=data_desconto['current_value'],
            delta=data_desconto['yoy_delta'],
            delta_color="inverse"
        )
        st.markdown(f"**Ano Ant. ({selected_year - 1}):** {data_desconto['previous_value']}")
        st.markdown(f"**YoY:** {data_desconto['yoy']}")
        fig_desc = create_sparkline(df_filtered, kpi_fixed_1, selected_year, selected_year - 1)
        st.plotly_chart(fig_desc, use_container_width=True, config={'displayModeBar': False})
            
    # CARD 3: MARGEM
    with col3:
        st.metric(
            label=f"💰 {kpi_fixed_2} ({selected_year})",
            value=data_margem['current_value'],
            delta=data_margem['yoy_delta'],
            delta_color="normal"
        )
        st.markdown(f"**Ano Ant. ({selected_year - 1}):** {data_margem['previous_value']}")
        st.markdown(f"**YoY:** {data_margem['yoy']}")
        fig_marg = create_sparkline(df_filtered, kpi_fixed_2, selected_year, selected_year - 1)
        st.plotly_chart(fig_marg, use_container_width=True, config={'displayModeBar': False})

    st.markdown("---")
    st.subheader("Análise Gráfica")

    # Filtrar dados para o ano atual e anterior
    df_current_and_previous = apply_filters(
        df, selected_year, selected_months, selected_brands, 
        selected_categories, selected_subcategories, selected_products
    )
    df_current_year = df_current_and_previous[df_current_and_previous['Ano'] == selected_year].copy()

    col4, col5 = st.columns([1, 1])
    
    with col4:
        fig_pie = create_pie_chart(df_current_year, selected_measure)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col5:
        fig_bar = create_bar_chart(df_current_year, selected_measure)
        st.plotly_chart(fig_bar, use_container_width=True)
        
    st.markdown("---")

    st.subheader("Sazonalidade Mensal (YoY)")
    fig_line = create_line_chart(df_current_and_previous, selected_measure, selected_year)
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.markdown("---")

    # -------------------------------------------------------
    # TABELA HIERÁRQUICA (Categoria -> Subcategoria -> Produto)
    # -------------------------------------------------------
    st.subheader("Visualização Hierárquica (Categoria/Subcategoria/Produto)")
    
    df_compare = df_current_and_previous 
    col_current = selected_year
    col_previous = selected_year - 1
    
    total_sales_current_year = df_current_year[selected_measure].sum() 
    
    df_cat_agg = df_compare.groupby(['Categoria', 'Ano'])[selected_measure].sum().reset_index()
    df_cat_pivot = df_cat_agg.pivot(index='Categoria', columns='Ano', values=selected_measure).fillna(0).reset_index()
    
    df_cat_pivot = df_cat_pivot.rename(columns={col_current: 'Valor_Atual', col_previous: 'Valor_Anterior'})

    if total_sales_current_year > 0:
        df_cat_pivot['Contribuicao_Cat'] = (df_cat_pivot['Valor_Atual'] / total_sales_current_year)
    else:
        df_cat_pivot['Contribuicao_Cat'] = 0

    df_cat_pivot = df_cat_pivot.sort_values(by='Valor_Atual', ascending=False)
    
    for index_cat, row_cat in df_cat_pivot.iterrows():
        cat = row_cat['Categoria']
        val_atual_cat = row_cat['Valor_Atual']
        val_anterior_cat = row_cat['Valor_Anterior']
        perc_cont_cat = row_cat['Contribuicao_Cat']
        
        perc_fmt_cat = f"{perc_cont_cat:.2%}" 
        title_expander = f"📦 Categoria: **{cat}** | Contribuição Total: **{perc_fmt_cat}**"
        
        with st.expander(title_expander):
            
            if val_anterior_cat != 0:
                yoy = ((val_atual_cat - val_anterior_cat) / val_anterior_cat)
                yoy_fmt = f"{yoy:+.2%}"
            else:
                yoy_fmt = "N/A"
            
            val_atual_fmt = f"R$ {val_atual_cat:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
            val_anterior_fmt = f"R$ {val_anterior_cat:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
            
            summary_data = {
                f"{selected_year} ({selected_measure})": [val_atual_fmt],
                f"{selected_year - 1} ({selected_measure})": [val_anterior_fmt],
                "Variação YoY": [yoy_fmt]
            }
            df_summary = pd.DataFrame(summary_data)
            st.markdown(f"#### Comparativo Categoria ({selected_measure})")
            st.dataframe(df_summary, hide_index=True, use_container_width=True)
            st.markdown("---")

            df_sub_agg = df_compare[df_compare['Categoria'] == cat]
            df_sub_agg = df_sub_agg.groupby(['Subcategoria', 'Ano'])[selected_measure].sum().reset_index()
            df_sub_pivot = df_sub_agg.pivot(index='Subcategoria', columns='Ano', values=selected_measure).fillna(0).reset_index()
            
            df_sub_pivot = df_sub_pivot.rename(columns={col_current: 'Valor_Atual', col_previous: 'Valor_Anterior'})
            
            if val_atual_cat > 0:
                df_sub_pivot['Contribuicao_Sub'] = (df_sub_pivot['Valor_Atual'] / val_atual_cat)
            else:
                df_sub_pivot['Contribuicao_Sub'] = 0
            
            df_sub_pivot = df_sub_pivot.sort_values(by='Valor_Atual', ascending=False)

            for index_sub, row_sub in df_sub_pivot.iterrows():
                sub = row_sub['Subcategoria']
                val_atual_sub = row_sub['Valor_Atual']
                val_anterior_sub = row_sub['Valor_Anterior']
                perc_cont_sub = row_sub['Contribuicao_Sub']
                
                perc_fmt_sub = f"{perc_cont_sub:.2%}"
                val_atual_sub_fmt = f"R$ {val_atual_sub:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
                
                st.markdown(f"** &nbsp; &nbsp; &nbsp; ↳ Subcategoria:** *{sub}* | **Contribuição Categoria:** {perc_fmt_sub} | **Valor ({selected_year}):** {val_atual_sub_fmt}")

                df_prod_agg = df_compare[
                    (df_compare['Categoria'] == cat) & 
                    (df_compare['Subcategoria'] == sub)
                ]
                df_prod_agg = df_prod_agg.groupby(['Descricao_Produto', 'Ano'])[selected_measure].sum().reset_index()
                df_prod_pivot = df_prod_agg.pivot(index='Descricao_Produto', columns='Ano', values=selected_measure).fillna(0).reset_index()
                
                df_prod_pivot = df_prod_pivot.rename(columns={col_current: 'Valor_Atual', col_previous: 'Valor_Anterior'})

                if val_atual_sub > 0:
                    df_prod_pivot['Contribuicao_Prod'] = (df_prod_pivot['Valor_Atual'] / val_atual_sub)
                else:
                    df_prod_pivot['Contribuicao_Prod'] = 0
                
                df_prod_pivot['Valor_Atual'] = df_prod_pivot['Valor_Atual'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
                df_prod_pivot['Valor_Anterior'] = df_prod_pivot['Valor_Anterior'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
                df_prod_pivot['Contribuicao_Prod'] = df_prod_pivot['Contribuicao_Prod'].apply(lambda x: f"{x:.2%}")
                
                df_prod_pivot = df_prod_pivot.rename(columns={
                    'Descricao_Produto': 'Produto',
                    'Valor_Atual': f'Valor {selected_year}',
                    'Valor_Anterior': f'Valor {selected_year - 1}',
                    'Contribuicao_Prod': 'Contribuição (%)'
                })
                
                st.dataframe(df_prod_pivot.set_index('Produto'), use_container_width=True)

    return df_current_and_previous
