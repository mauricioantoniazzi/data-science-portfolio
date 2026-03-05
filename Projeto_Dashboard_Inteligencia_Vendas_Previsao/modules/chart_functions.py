import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from math import pi

def create_sparkline(df_monthly, measure, current_year, previous_year):
    """
    Cria um gráfico de linha pequeno (Sparkline) para mostrar a evolução mensal de um KPI.
    """
    # Garantir que a coluna 'Mes' esteja ordenada corretamente (1 a 12)
    df_chart = df_monthly.sort_values(by='Mes')

    # Renomear 'Ano' para a legenda
    df_chart['Ano_Label'] = df_chart['Ano'].astype(str)
    
    # ⚠️ Ajuste: Se for Margem, calcular a média mensal, senão, usar a soma
    if measure == 'Margem':
        # Se Margem for em %, é melhor visualizar a média mensal da %
        aggregation_func = 'mean'
    elif measure == 'Quantidade':
        aggregation_func = 'sum'
    else:
        # Para R$, usa-se a soma
        aggregation_func = 'sum'
        
    # Agrupar os dados por Mês e Ano, aplicando a agregação correta
    df_grouped = df_chart.groupby(['Ano', 'Mes', 'Ano_Label'])[measure].agg(aggregation_func).reset_index()

    # O Plotly é usado com configurações mínimas para se parecer com um Sparkline
    fig = px.line(
        df_grouped,
        x='Mes',
        y=measure,
        color='Ano_Label',
        line_dash='Ano_Label', # Adiciona tracejado para o ano anterior
        height=150,
        labels={'Mes': '', measure: ''},
        title=f"Evolução Mensal: {current_year} vs {previous_year}",
        color_discrete_map={str(current_year): 'green', str(previous_year): 'gray'}
    )

    # Ocultar eixos, legenda e modo de barra para um estilo Sparkline
    fig.update_layout(
        showlegend=False,
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis={'visible': False, 'showgrid': False},
        yaxis={'visible': False, 'showgrid': False},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified"
    )
    
    # Adicionar o título do ano atual e anterior na linha
    fig.update_traces(mode='lines+markers', marker=dict(size=4))
    
    return fig

def create_pie_chart(df, measure, title="Distribuição por Canal"):
    """Cria um gráfico de pizza da Medida Selecionada pela Descricao_Canal."""
    
    # 1. Agregação: Soma a Medida por Canal
    df_agg = df.groupby('Descricao_Canal')[measure].sum().reset_index()
    
    # 2. Criação do Gráfico
    fig = px.pie(
        df_agg,
        values=measure,
        names='Descricao_Canal',
        title=f'{title} de {measure}',
        hole=.3,  # Cria um gráfico de rosca
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    # 3. Formatação
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True,
        # Centraliza o título no gráfico de rosca
        title_x=0.5
    )
    return fig

def create_bar_chart(df, measure, title="Ranking por Marca (Top 10)"):
    """Cria um gráfico de barras horizontal (Ranking) da Medida Selecionada por Marca."""
    
    # 1. Agregação e Ranking (Top 10)
    df_agg = df.groupby('Marca')[measure].sum().reset_index()
    df_agg = df_agg.sort_values(by=measure, ascending=False).head(10)
    
    # 2. Criação do Gráfico
    fig = px.bar(
        df_agg,
        x=measure,
        y='Marca',
        orientation='h', # Barras horizontais
        title=f'{title} de {measure}',
        color=measure,
        color_continuous_scale=px.colors.sequential.Plotly3
    )
    
    # 3. Formatação
    fig.update_yaxes(autorange="reversed") # Garante que o item com maior valor fique no topo
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis_title=measure,
        yaxis_title="",
        coloraxis_showscale=False # Oculta a barra lateral de cores
    )
    return fig

def create_line_chart(df, measure, current_year, title="Sazonalidade Mensal"):
    """Cria um gráfico de linhas de evolução mensal (Ano Atual vs Ano Anterior)."""
    
    # 1. Agregação e Preparação
    # Garantir que a agregação está correta (Média para Margem, Soma para o resto)
    if measure == 'Margem':
        agg_method = 'mean'
    elif measure == 'Quantidade':
        agg_method = 'sum'
    else:
        agg_method = 'sum'
        
    df_monthly = df.groupby(['Ano', 'Mes'])[measure].agg(agg_method).reset_index()
    
    # Converter o número do mês para nome, garantindo a ordenação correta do eixo X
    df_monthly['Nome_Mes'] = df_monthly['Mes'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%b'))

    # 2. Criação do Gráfico
    fig = px.line(
        df_monthly,
        x='Nome_Mes',
        y=measure,
        color='Ano',
        title=f'{title} de {measure}',
        # Garante que o ano atual e anterior tenham cores diferentes
        color_discrete_map={
            current_year: '#1f77b4', # Ex: Azul para ano atual
            current_year - 1: '#aaaaaa' # Ex: Cinza para ano anterior
        }
    )
    
    # 3. Formatação
    # Ordenar o eixo X (meses) corretamente
    ordered_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig.update_xaxes(categoryarray=ordered_months)
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        legend_title_text='Ano',
        hovermode="x unified"
    )
    
    return fig