# 🏭 Análise de Dados de Engenharia de Produção: Previsão e Detecção de Anomalias com Power BI

Este projeto é um dashboard de **Análise de Dados de Produção**, desenvolvido no **Power BI Desktop**, com o objetivo de manipular e compreender dados de unidades produzidas, explorando conceitos avançados de **Análise de Séries Temporais**. O painel realiza a previsão de unidades produzidas para os próximos 5 anos e identifica anomalias nos dados históricos.

---

### 🎯 Objetivo do Projeto

O objetivo principal deste dashboard é fornecer insights sobre o desempenho da produção e auxiliar no planejamento estratégico, utilizando técnicas de séries temporais. O painel foi construído para:

* **Analisar a Média de Unidades Produzidas** por diferentes dimensões de tempo (Ano, Trimestre, Mês) e fatores de produção (Faixa Etária dos Funcionários, Turno).
* **Realizar Previsões** de unidades produzidas para um horizonte de 5 anos, auxiliando no planejamento futuro.
* **Detectar Anomalias** nos dados históricos de produção, indicando eventos incomuns que podem necessitar de investigação.
* **Fornecer filtros interativos** para explorar os dados sob diversas perspectivas.

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`Producao`) que contém informações sobre as unidades produzidas, o período e características da força de trabalho. As principais colunas da base de dados são:

* **Tempo**: `Período` (contém a data das observações de produção).
* **Produção**: `Total Unidades Produzidas`.
* **Recursos Humanos**: `Range Idade Funcionários` e `Turno`.

Uma medida DAX, `Média móvel de Soma de Total Unidades Produzidas`, foi criada para suavizar as tendências nos dados.

---

### ✨ Métricas e Análises Principais

O dashboard oferece uma visão abrangente sobre o processo produtivo, com as seguintes métricas e análises:

* **Média de Unidades Produzidas (Anual, Trimestral, Mensal)**: Um gráfico de área que mostra a **Média de Unidades Produzidas** segmentada por `Faixa Etária dos Funcionários` e com drill-down para diferentes níveis de tempo. Filtros por `Turno` e `Faixa Etária` permitem análises personalizadas.
* **Detecção de Anomalias**: Um gráfico de linha que automaticamente identifica e destaca **pontos fora do padrão** nos dados de produção, alertando sobre possíveis eventos incomuns ou erros.
* **Previsões de Unidades Produzidas**: Um gráfico de linha que projeta as **Previsões de Unidades Produzidas com Horizonte de 5 anos**, incluindo um intervalo de confiança para a previsão, auxiliando no planejamento de longo prazo.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **Power Query**: Utilizado para carregar e realizar transformações e limpezas nos dados.
* **DAX (Data Analysis Expressions)**: Usado para criar medidas, como a `Média móvel de Soma de Total Unidades Produzidas`, essencial para a análise de séries temporais.
* **Análise de Séries Temporais**: Exploração de recursos nativos do Power BI para **Previsão** e **Detecção de Anomalias**, que são pilares da análise de séries temporais.
* **Filtros Interativos**: Implementação de filtros por `Turno` e `Faixa Etária dos Funcionários` para permitir análises dinâmicas e detalhadas.

---