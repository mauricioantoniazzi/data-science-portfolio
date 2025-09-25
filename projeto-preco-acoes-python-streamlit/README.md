# 📈 Dashboard de Acompanhamento de Ativos Financeiros

Este projeto consiste na criação de um aplicativo interativo para o acompanhamento e análise de performance de uma carteira de ações e outros ativos do mercado financeiro. Desenvolvido com **Streamlit**, o dashboard permite aos usuários visualizar o histórico de cotações, aplicar filtros dinâmicos e calcular a performance de ativos individuais ou de um portfólio completo.

O objetivo é fornecer uma ferramenta de análise completa, semelhante às telas de corretoras, com funcionalidades de comparação e simulação de períodos.

## ✨ Funcionalidades Principais

  * **Carregamento de Tickers:** O sistema carrega automaticamente todas as ações do índice Bovespa (I-BOV) a partir de um arquivo de dados (`ibov.csv`).
  * **Seleção Múltipla de Ativos:** Utilize a barra lateral para selecionar dinamicamente quais ativos deseja visualizar no gráfico.
  * **Gráfico de Linha Interativo:** Visualize a evolução histórica das cotações selecionadas com um gráfico que suporta zoom e navegação temporal.
  * **Filtro de Período:** Analise a performance dos ativos em intervalos de tempo específicos, como "2020 até o momento".
  * **Análise de Performance Individual:** O dashboard calcula a performance percentual de cada ativo no período selecionado.
  * **Formatação Visual:** Os resultados percentuais são exibidos em cores (verde para desempenho positivo e vermelho para negativo) para facilitar a visualização.
  * **Performance da Carteira:** Calcule a performance total de uma carteira simulada, considerando uma alocação de peso igual para cada ativo (ex: R$ 1.000 por ativo).
  * **Eficiência (Caching):** O uso do decorador `@st.cache_data` otimiza o desempenho do aplicativo, evitando o recálculo constante dos dados.
  * **Aparência (Dark Mode):** O aplicativo é configurado para rodar em Dark Mode para uma melhor experiência visual.

### 💻 Tecnologias Utilizadas

* **Python**
    * Linguagem de programação principal.
* **Streamlit**
    * Framework para a construção do dashboard e da interface.
* **Pandas**
    * Manipulação e filtragem de DataFrames de cotações.
* **Yfinance**
    * Obtenção de dados históricos de cotações de ativos.
* **Markdown**
    * Formatação de textos e títulos no Streamlit.
* **TOML**
    * Arquivo de configuração visual (`config.toml`) para temas.

## 🚀 Configuração e Execução

### 1\. Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina.

### 2\. Instalação das Bibliotecas

Abra seu terminal ou prompt de comando e instale as bibliotecas necessárias:

```bash
pip install streamlit
pip install pandas
pip install yfinance
```

### 3\. Execução do Aplicativo

Navegue até o diretório onde o arquivo principal do projeto (`main.py`) e os arquivos de dados (`ibov.csv`) estão localizados. Em seguida, execute o Streamlit com o seguinte comando:

```bash
streamlit run main.py
```

O aplicativo será iniciado automaticamente em seu navegador web. O processo de execução é contínuo, o que permite que as edições no código sejam refletidas após o salvamento e um *rerun*.

### 4\. Configuração Visual (Dark Mode)

Para habilitar o Dark Mode, o projeto deve conter uma pasta `.streamlit` no mesmo nível do arquivo principal. Dentro dela, crie um arquivo chamado `config.toml` com o seguinte conteúdo:

```toml
[theme]
base = "dark"
```

## 🌐 Deploy

Para tornar o aplicativo acessível globalmente, você pode realizar o processo de **Deploy** utilizando a comunidade Streamlit (pelo botão "Deploy Now" na interface), que geralmente oferece um serviço gratuito para aplicativos públicos.