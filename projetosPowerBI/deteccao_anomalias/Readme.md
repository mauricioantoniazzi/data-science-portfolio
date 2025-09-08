# 🕵️ Detecção de Anomalias em Transações Financeiras com Machine Learning e Power BI

Este projeto é um dashboard de **Detecção de Anomalias**, desenvolvido no **Power BI Desktop**, com o objetivo de identificar potenciais transações fraudulentas em dados financeiros de clientes. Utilizando **Machine Learning**, o projeto agrupa os dados de transações e, em seguida, detecta e define as anomalias, fornecendo uma visualização clara dos resultados.

---

### 🎯 Objetivo do Projeto

O objetivo principal deste projeto é investigar e revelar a existência de anomalias (potenciais fraudes) em um conjunto de dados de transações financeiras. O dashboard foi construído para:

* **Aplicar técnicas de Machine Learning** para classificar transações como "normal" ou "anomalia".
* **Visualizar a distribuição das anomalias** e seus scores correspondentes.
* **Fornecer métricas claras** sobre a proporção de anomalias encontradas.
* **Integrar análises estatísticas avançadas** (como Box Plot) utilizando a linguagem R no Power BI.

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`previsoes_novos_dados`) que contém informações de transações financeiras de clientes. As principais colunas da base de dados são:

* `id`: Identificador único da transação.
* `anomaly_score`: Score gerado pelo modelo de Machine Learning, indicando a probabilidade de uma transação ser anômala (quanto maior, maior a anomalia).
* `status`: Classificação final da transação (`normal` ou `anomalia`).
* `average_depth` e `Column1`: Outras variáveis que podem ter sido usadas na geração do `anomaly_score`.

---

### ✨ Métricas e Análises Principais

O dashboard oferece uma visão abrangente sobre a detecção de anomalias, com as seguintes métricas e análises:

* **Total de Registros Por Score de Anomalia**: Um gráfico de barras que mostra a distribuição dos scores de anomalia, permitindo visualizar a concentração dos valores e identificar onde as anomalias se destacam.
* **Total de Registros por Status**: Um gráfico de pizza que exibe a proporção percentual de transações classificadas como `normal` ou `anomalia`, oferecendo uma visão imediata da dimensão do problema.
* **Média e Maior Score de Anomalia**: Cartões de indicadores que apresentam a **Média do Score de Anomalia** e o **Maior Score de Anomalia** encontrado, fornecendo resumos importantes para avaliação.
* **Box Plot de Scores por Status (Gráfico R)**: Um gráfico Box Plot avançado, criado com a **linguagem R** e integrado ao Power BI, que compara visualmente a distribuição dos scores de anomalia entre as transações `anomalia` e `normal`, destacando as diferenças estatísticas entre os grupos.
* **Média do Score de Anomalia Por Status**: Um gráfico de barras simples que compara a média dos scores de anomalia entre as transações normais e as anômalas.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do dashboard e visualização dos resultados.
* **Machine Learning**: Utilizado na fase pré-Power BI para agrupar e classificar as transações, gerando o `anomaly_score` e o `status`.
* **Linguagem R**: Integrada ao Power BI para a criação do **Box Plot**, permitindo análises estatísticas mais complexas e visuais específicos.
* **Power Query**: Utilizado para carregar e preparar os dados de entrada no Power BI.
* **DAX (Data Analysis Expressions)**: Usado para criar medidas, como a média dos scores, e para garantir a agregação correta dos dados.

---