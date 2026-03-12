import streamlit as st
from modules.kpi_calculations import apply_filters, calculate_kpis, get_hierarchical_data, get_subcat_data
from modules.ui_components import render_kpi_card, render_summary_table, format_currency
from modules.chart_functions import create_sparkline, create_pie_chart, create_bar_chart, create_line_chart

def render_visao_geral(df, filters):
    year = filters['year']
    measure = filters['measure']
    
    # 1. Dados Filtrados
    df_filtered = apply_filters(df, year, filters['months'], filters['brands'], 
                                filters['categories'], filters['subcategories'], filters['products'])
    
    # 2. Seção de KPIs
    col1, col2, col3 = st.columns(3)
    
    metrics = [
        (col1, f"⭐ {measure}", measure, False, "principal"),
        (col2, "💸 Desconto", "Desconto", True, "desconto"),
        (col3, "💰 Margem", "Margem", False, "margem")
    ]
    
    for col, title, m_name, inv, key_suffix in metrics:
        with col:
            data = calculate_kpis(df_filtered, year, m_name)
            render_kpi_card(f"{title} ({year})", data, m_name, is_inverse=inv)
            fig = create_sparkline(df_filtered, m_name, year, year - 1)
            st.plotly_chart(
                fig, use_container_width=True,
                config={'displayModeBar': False},
                key=f"sparkline_{m_name}_{key_suffix}"
            )

    st.divider()

    # 3. Análise Gráfica
    st.subheader("Análise Gráfica")
    df_curr = df_filtered[df_filtered['Ano'] == year]
    
    c4, c5 = st.columns(2)
    c4.plotly_chart(create_pie_chart(df_curr, measure), use_container_width=True)
    c5.plotly_chart(create_bar_chart(df_curr, measure), use_container_width=True)
    
    st.subheader("Sazonalidade Mensal (YoY)")
    st.plotly_chart(create_line_chart(df_filtered, measure, year), use_container_width=True)

    st.divider()

    # 4. Tabela Hierárquica
    st.subheader("Visualização Hierárquica")
    df_cat = get_hierarchical_data(df_filtered, measure, year)

    for _, row in df_cat.iterrows():
        title = f"📦 Categoria: **{row['Categoria']}** | Contribuição: **{row['contribution']:.2%}**"
        
        with st.expander(title):
            render_summary_table(row['val_curr'], row['val_prev'], year)
            
            # Subcategorias
            df_sub = get_subcat_data(df_filtered, row['Categoria'], measure, year)
            for _, s_row in df_sub.sort_values('val_curr', ascending=False).iterrows():
                st.markdown(f"&nbsp;&nbsp;&nbsp; ↳ **Sub:** {s_row['Subcategoria']} | **Valor:** {format_currency(s_row['val_curr'])}")