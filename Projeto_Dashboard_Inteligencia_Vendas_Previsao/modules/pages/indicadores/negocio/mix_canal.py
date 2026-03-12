import streamlit as st
import pandas as pd
import plotly.express as px
from modules.core.db_connector import run_query

def render_mix_canal():
  st.subheader("🏪 Comparativo de Mix: Loja vs Online")
  df_mix = run_query("SELECT * FROM mart_mix_por_canal")

  if not df_mix.empty:
      # 1. Gráfico de Barras
      fig_mix = px.bar(
          df_mix, 
          x='Descricao_Canal', 
          y='pct_representatividade_no_canal', 
          color='Categoria', 
          barmode='group',
          title="Representatividade de Categorias por Canal (%)",
          labels={'pct_representatividade_no_canal': '% Representatividade', 'Descricao_Canal': 'Canal'}
      )
      st.plotly_chart(fig_mix, use_container_width=True)

      st.markdown("---")
      st.write("🔍 **Detalhamento por Canal e Ticket Médio**")

      # 2. Preparação dos dados para exibição
      df_display = df_mix.copy()

      # Formatação de Moeda e Porcentagem
      def format_brl(val):
          return f"R$ {val:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

      df_display['faturamento_canal_cat'] = df_display['faturamento_canal_cat'].apply(format_brl)
      df_display['faturamento_total_do_canal'] = df_display['faturamento_total_do_canal'].apply(format_brl)
      df_display['ticket_medio_canal_cat'] = df_display['ticket_medio_canal_cat'].apply(format_brl) # Formata Ticket Médio
      df_display['pct_representatividade_no_canal'] = df_display['pct_representatividade_no_canal'].apply(lambda x: f"{x:.1f}%")

      # 3. Renderização com Nomes Amigáveis
      st.dataframe(
          df_display, 
          column_config={
              "Descricao_Canal": "Canal de Venda",
              "Categoria": "Categoria de Produto",
              'qtd_pedidos': "Qtd Pedidos",
              "faturamento_canal_cat": "Faturamento (Cat)",
              "faturamento_total_do_canal": "Total do Canal",
              "pct_representatividade_no_canal": "% Mix",
              "ticket_medio_canal_cat": "Ticket Médio"
          },
          hide_index=True, 
          use_container_width=True
      )