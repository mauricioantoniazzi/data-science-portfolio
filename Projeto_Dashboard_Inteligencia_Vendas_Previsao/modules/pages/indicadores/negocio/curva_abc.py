import streamlit as st
import pandas as pd
import plotly.express as px
from modules.db_connector import run_query

def render_curva_abc():
  st.subheader("Análise de Pareto (Curva ABC)")
  # Busca a MART criada pelo dbt
  df_abc = run_query("SELECT * FROM mart_curva_abc_produtos ORDER BY pct_acumulado")
  print(f'resultado query: {df_abc.shape[0]} linhas')
  if not df_abc.empty:
      col_a, col_b, col_c = st.columns(3)
      # KPI Rápidos da Curva
      total_a = len(df_abc[df_abc['classificacao_abc'] == 'A'])
      total_b = len(df_abc[df_abc['classificacao_abc'] == 'B'])
      total_c = len(df_abc[df_abc['classificacao_abc'] == 'C'])

      # Cálculo de representatividade (opcional, mas ajuda muito)
      total_geral = len(df_abc)

      with col_a:
          st.metric(
              label="🏆 Classe A (80%)", 
              value=total_a, 
              help="Produtos que geram a maior parte do faturamento."
          )
          st.caption(f"{total_a/total_geral:.1%} do catálogo")

      with col_b:
          st.metric(
              label="🥈 Classe B (15%)", 
              value=total_b, 
              help="Produtos de importância intermediária."
          )
          st.caption(f"{total_b/total_geral:.1%} do catálogo")

      with col_c:
          st.metric(
              label="🥉 Classe C (5%)", 
              value=total_c, 
              help="A 'cauda longa': muitos produtos com baixo faturamento individual."
          )
          st.caption(f"{total_c/total_geral:.1%} do catálogo")

      # Pegando uma amostra de cada classe para o gráfico
      # df_grafico = pd.concat([
      #     df_abc[df_abc['classificacao_abc'] == 'A'].head(10),
      #     df_abc[df_abc['classificacao_abc'] == 'B'].head(5),
      #     df_abc[df_abc['classificacao_abc'] == 'C'].head(5)
      # ])

      # Gráfico de Pareto
      # fig_abc = px.bar(
      #     df_grafico, 
      #     x='Descricao_Produto', 
      #     y='faturamento_item', 
      #     color='classificacao_abc', 
      #     title="Comparativo de Classes (Top de cada Categoria)",
      #     color_discrete_map={'A': '#2E7D32', 'B': '#FBC02D', 'C': '#D32F2F'} # Verde, Amarelo, Vermelho
      # )
      # st.plotly_chart(fig_abc, use_container_width=True)

      # Substitua o px.bar por este para um visual "Uau":
      fig_abc = px.treemap(
          df_abc, 
          path=['classificacao_abc', 'Categoria', 'Descricao_Produto'], 
          values='faturamento_item',
          color='classificacao_abc',
          color_discrete_map={'A': '#2E7D32', 'B': '#FBC02D', 'C': '#D32F2F'},
          title="Distribuição do Mix de Produtos por Classe ABC"
      )
      st.plotly_chart(fig_abc, use_container_width=True)

      # Cria uma cópia para não estragar o gráfico com strings
      df_display = df_abc.copy()
      
      # Formata faturamento como R$ 1.234,56
      df_display['faturamento_item'] = df_display['faturamento_item'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "v").replace(".", ",").replace("v", "."))
      # Formata acumulado como 85.5%
      df_display['pct_acumulado'] = df_display['pct_acumulado'].apply(lambda x: f"{x:.1f}%")

      st.dataframe(
          df_display[['Descricao_Produto', 'Categoria', 'faturamento_item', 'classificacao_abc', 'pct_acumulado']], 
          column_config={
            "Descricao_Produto": "Produto",
            "faturamento_item": "Faturamento Total",
            "classificacao_abc": "Classe",
            "pct_acumulado": "% Acumulada"
          },
          hide_index=True, 
          use_container_width=True
      )