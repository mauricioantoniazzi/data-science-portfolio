# ==============================================================================
# ITEM 4: PREVISÃO (FORECASTING)
# ==============================================================================

import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly


def render_item4(df, filters):
    """
    Renderiza o Item 4: Previsão de Vendas usando Prophet
    
    Args:
        df: DataFrame completo de vendas
        filters: Dicionário com os filtros selecionados
    """
    
    selected_measure = filters['measure']
    
    st.header("Previsão de Vendas/Volume por Categoria (Prophet)")
    st.markdown("---")

    # Validar coluna de data
    if 'Data' not in df.columns:
        st.error("O DataFrame precisa da coluna 'Data' no formato datetime para a previsão.")
        return
    
    # Agregação MENSAL
    df_prophet = df.groupby([df['Data'].dt.to_period('M'), 'Categoria'])[selected_measure].sum().reset_index()
    df_prophet['Data'] = df_prophet['Data'].dt.to_timestamp()
    
    # Renomear para padrão Prophet
    df_prophet.rename(columns={'Data': 'ds', selected_measure: 'y'}, inplace=True)
    
    # Parâmetros de previsão
    forecast_periods = st.slider("Meses de Previsão:", min_value=3, max_value=24, value=12)
    
    # Obter categorias únicas
    categories = df_prophet['Categoria'].unique()
    
    st.markdown("#### Detalhamento da Previsão por Categoria")
    
    for category in categories:
        df_cat = df_prophet[df_prophet['Categoria'] == category].drop(columns=['Categoria'])
        
        # Validar dados suficientes
        if len(df_cat) < 24:
            st.warning(f"⚠️ **{category}** - Dados insuficientes (menos de 24 meses) para uma previsão robusta com sazonalidade anual.")
            continue
        
        # Configurar e treinar modelo
        m = Prophet(
            seasonality_mode='multiplicative',
            yearly_seasonality=True,
            daily_seasonality=False,
            weekly_seasonality=False
        )
        
        m.fit(df_cat)
        
        # Gerar previsão
        future = m.make_future_dataframe(periods=forecast_periods, freq='M')
        forecast = m.predict(future)
        
        # Visualizar
        st.markdown(f"##### 📊 Categoria: **{category}**")
        
        fig = plot_plotly(m, forecast, uncertainty=True)
        fig.update_layout(
            yaxis_tickformat='.2f',
            xaxis_title="Data",
            yaxis_title=f"{selected_measure}",
            title=f"Previsão ({selected_measure}) vs Realizado - {category}"
        )

        st.plotly_chart(fig, use_container_width=True)
        st.markdown("---")

        # Análise de componentes
        with st.expander(f"🔎 Analisar Drivers da Previsão para {category}"):
            
            st.markdown("###### Decomposição do Modelo (Tendência e Sazonalidade)")
            st.caption("Esta figura mostra a Tendência de longo prazo e a Sazonalidade Anual capturada pelo modelo.")
            
            fig_components = m.plot_components(forecast)
            st.pyplot(fig_components, clear_figure=True) 

        st.markdown(f"***")

    st.success("Previsões concluídas para todas as categorias com dados suficientes!")
