# ==============================================================================
# ITEM 1: PRINCIPAIS INDICADORES
# ==============================================================================

import streamlit as st
from modules.pages.insights.visao_geral import render_visao_geral
from modules.pages.insights.curva_abc import render_curva_abc
from modules.pages.insights.saude_cliente import render_saude_cliente
from modules.pages.insights.mix_canal import render_mix_canal

def render_principais_indicadores(df, filters):
    st.title("🚀 Inteligência de Vendas")

    # Criação das Abas para organizar as perguntas de negócio
    tab_geral, tab_abc, tab_clientes, tab_canais = st.tabs([
        "📊 Visão Geral", 
        "📦 Curva ABC", 
        "👥 Saúde do Cliente (RF)", 
        "🏪 Mix por Canal"
    ])

    # ------------------------------------------------------------------
    # ABA 1: VISÃO GERAL (Seu código atual)
    # ------------------------------------------------------------------
    with tab_geral:
        render_visao_geral(df, filters)

    # ------------------------------------------------------------------
    # ABA 2: CURVA ABC (Pergunta 1)
    # ------------------------------------------------------------------
    with tab_abc:
        render_curva_abc()
     
    # ------------------------------------------------------------------
    # ABA 3: SAÚDE DO CLIENTE (Pergunta 2)
    # ------------------------------------------------------------------
    with tab_clientes:
        render_saude_cliente()
        
    # ------------------------------------------------------------------
    # ABA 4: MIX POR CANAL (Pergunta 3)
    # ------------------------------------------------------------------
    with tab_canais:
        render_mix_canal()
