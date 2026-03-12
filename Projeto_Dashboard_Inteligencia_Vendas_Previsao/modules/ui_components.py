import streamlit as st
import pandas as pd

def format_currency(val):
    return f"R$ {val:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")

def render_kpi_card(title, data, measure_name, is_inverse=False):
    """Renderiza o card de métrica com sparkline."""
    delta_color = "inverse" if is_inverse else "normal"
    
    st.metric(
        label=title,
        value=data['current_value'],
        delta=data['yoy_delta'],
        delta_color=delta_color
    )
    st.caption(f"**Ano Ant.:** {data['previous_value']} | **YoY:** {data['yoy']}")

def render_summary_table(val_curr, val_prev, year):
    """Tabela comparativa simples dentro do expander."""
    yoy = ((val_curr - val_prev) / val_prev) if val_prev != 0 else 0
    df_sum = pd.DataFrame({
        f"{year}": [format_currency(val_curr)],
        f"{year-1}": [format_currency(val_prev)],
        "Variação YoY": [f"{yoy:+.2%}"]
    })
    st.dataframe(df_sum, hide_index=True, use_container_width=True)