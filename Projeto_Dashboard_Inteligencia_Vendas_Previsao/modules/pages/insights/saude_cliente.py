import streamlit as st
import pandas as pd
import plotly.express as px
from modules.core.db_connector import run_query

def render_saude_cliente():
  st.subheader("👥 Segmentação por Recência e Frequência (RF)")
  df_rf = run_query("SELECT * FROM mart_segmentacao_rf")

  if not df_rf.empty:
      # 1. Gráfico de Rosca (Donut)
      fig_rf = px.pie(
          df_rf, 
          names='status_cliente', 
          values='faturamento_historico',
          title="Distribuição do Faturamento por Perfil de Cliente", 
          hole=0.4,
          color_discrete_sequence=px.colors.qualitative.Pastel
      )
      st.plotly_chart(fig_rf, use_container_width=True)
      
      # 2. Seção de Alerta: Clientes em Risco
      st.markdown("---")
      st.markdown("### 🚨 Top 10 Clientes Críticos para Recuperação")
      
      # Filtra clientes em Risco ou Perdidos e ordenamos pelos que não compram há mais tempo
      df_risco = df_rf[df_rf['status_cliente'].str.contains("Risco|Perdido", case=False)].copy()
      df_risco = df_risco.sort_values(by='dias_sem_comprar', ascending=False).head(10)

      if not df_risco.empty:
          # Formatação de Moeda
          df_risco['faturamento_historico'] = df_risco['faturamento_historico'].apply(
              lambda x: f"R$ {x:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
          )

          # Usamos st.dataframe em vez de st.table para aplicar cores e formatação rica
          st.dataframe(
              df_risco[['Nome_Cliente', 'status_cliente', 'dias_sem_comprar', 'total_pedidos', 'faturamento_historico']],
              column_config={
                  "Nome_Cliente": "Cliente",
                  "status_cliente": "Status",
                  "dias_sem_comprar": st.column_config.NumberColumn(
                      "Dias em Inatividade",
                      help="Dias desde a última compra",
                      format="%d d", # Adiciona o "d" de dias
                  ),
                  "total_pedidos": "Qtd Pedidos",
                  "faturamento_historico": "LTV (Valor Total)"
              },
              hide_index=True,
              use_container_width=True
          )
      else:
          st.success("✅ Nenhum cliente classificado como 'Em Risco' ou 'Perdido' no momento!")

      # 3. Lista de Clientes "Campeões" (Extra)
      with st.expander("🏆 Ver Clientes Campeões (Frequentes)"):
          df_campeoes = df_rf[df_rf['status_cliente'].str.contains("Campeão|Fiel", case=False)].head(10)
          st.dataframe(
              df_campeoes[['Nome_Cliente', 'status_cliente', 'total_pedidos']],
              column_config={
                  'Nome_Cliente': "Cliente",
                  'status_cliente': "Status",
                  'total_pedidos': "Qtd Pedidos"
              },
              use_container_width=True,
              hide_index=True)