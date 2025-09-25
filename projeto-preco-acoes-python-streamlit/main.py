# Importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

# criar funções de carregamento de dados
@st.cache_data
def carregar_dados(empresas):
  cotacoes_acao = yf.download(empresas, start="2010-01-01", end="2025-09-01")
  cotacoes_acao = cotacoes_acao["Close"]
  return cotacoes_acao

@st.cache_data
def carregar_tickers_acoes():
  base_tickers = pd.read_csv("IBOV_FILTER.csv", sep=";")
  # pegar somente o código dentro da tabela
  tickers = list(base_tickers["Código"])
  tickers = [item + ".SA" for item in tickers]
  return tickers

# preparar as visualizações
acoes = ["ITUB4.SA", "MGLU3.SA", "PETR4.SA", "VALE3.SA", "BBDC4.SA"]
# acoes = carregar_tickers_acoes()
dados = carregar_dados(acoes)
print(dados)

# Criar a interface do streamlit
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço de ações ao longo dos anos.
""")

#prepara as visualizações = filtros
st.sidebar.header("Filtros")

# filtro de ações
lista_acoes = st.sidebar.multiselect('Escolha as ações para visualizar', dados.columns)
if lista_acoes:
  dados = dados[lista_acoes]
  if len(lista_acoes) == 1:
    acao_unica = lista_acoes[0]
    dados = dados.rename(columns={acao_unica: "Close"})

# filtro por data
# como o index é a data podemos pegar a data inicial e final conforme abaixo
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider("Selecione o período", min_value=data_inicial, max_value=data_final,
                  value=(data_inicial, data_final))

dados = dados.loc[intervalo_data[0]: intervalo_data[1]]
# criar o grafico
st.line_chart(dados)

# Calculo de performance
texto_performance_ativos = ""

if len(lista_acoes)==0:
  lista_acoes = list(dados.columns)
elif len(lista_acoes)==1:
  dados = dados.rename(columns={"Close": acao_unica})

# Definindo carteira de ações
carteira = [1000 for acao in lista_acoes]
total_inicial_cateira = sum(carteira)

for i, acao in enumerate(lista_acoes):
  performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
  performance_ativo = float(performance_ativo)

  carteira[i] = carteira[i] * (1 + performance_ativo)

  if performance_ativo > 0:
    texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :green[{performance_ativo:.1%}]"
  elif performance_ativo < 0:
    texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :red[{performance_ativo:.1%}]"
  else:
    texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: {performance_ativo:.1%}"

total_final_cateira = sum(carteira)
performance_carteira = total_final_cateira / total_inicial_cateira - 1

if performance_carteira > 0:
  texto_performance_carteira = f"Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]"
elif performance_carteira < 0:
  texto_performance_carteira = f"Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]"
else:
  texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"

st.write(f"""
### Performance dos Ativos
Essa foi a performance de cada ativo no período selecionado:   
{texto_performance_ativos}

{texto_performance_carteira}
""")

