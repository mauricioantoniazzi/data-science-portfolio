# 📊 Análise de Dados do Mercado de Ações com Power BI

Este projeto é um dashboard de **Análise do Mercado de Ações**, desenvolvido no **Power BI Desktop**, com o objetivo de monitorar o desempenho de diferentes empresas ao longo do tempo. O painel foi criado para fornecer insights sobre o volume de negociações, preços das ações e tendências de mercado.

---

### 🎯 Objetivo do Projeto

O objetivo principal deste dashboard é transformar dados brutos do mercado de ações em **informações acionáveis** que apoiam a análise de investimentos. O painel foi construído para responder a perguntas de negócio essenciais, como:

* **Qual o volume total de ações negociadas ao longo do tempo para as empresas selecionadas?**
* **Como os preços (abertura, alta, baixa, fechamento) e o volume das ações variam mensalmente?**
* **Qual a variação da média do valor de fechamento das ações mês a mês?**
* **Quais são as principais tendências e características dos dados de mercado?**

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`StockMarket`) que contém informações históricas de negociação de ações para um conjunto de empresas. As principais colunas da base de dados são:

* **Identificação**: `Empresa`
* **Tempo**: `Data` (período de análise de 1 ano, aproximadamente de março de 2022 a março de 2023)
* **Preços das Ações**:
    * `Open` (Preço de Abertura)
    * `High` (Preço Máximo)
    * `Low` (Preço Mínimo)
    * `Close` (Preço de Fechamento)
* **Volume**: `Volume` de ações negociadas

Uma medida DAX, `Média de Close`, foi criada para auxiliar nas análises.

---

### ✨ Métricas e Análises Principais

O dashboard oferece uma visão abrangente sobre o desempenho das ações, com as seguintes métricas e análises:

* **Volume Total ao Longo do Tempo**: Um gráfico de linha que mostra o **volume total negociado de ações** para as empresas selecionadas, permitindo identificar picos e vales de atividade. Filtros por `Empresa` e `Mês` permitem análises customizadas.
* **Variação da Média de Fechamento (MoM)**: Um gráfico de área que ilustra a **variação mensal da média do valor de fechamento (Close)** das ações de todas as empresas, facilitando a visualização de tendências de alta e baixa.
* **Tabela de Valores Médios Por Mês**: Uma tabela detalhada que exibe o **valor médio de abertura, mais alto, mais baixo e de fechamento**, bem como o volume total de ações para cada mês do período analisado.
* **Narrativa Inteligente**: Um componente de texto dinâmico que gera automaticamente **explicações e insights** sobre as principais características e tendências nos dados, como variações de volume e tendências de média de fechamento.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **Power Query**: Utilizado para carregar e realizar transformações e limpezas nos dados.
* **DAX (Data Analysis Expressions)**: Usado para criar medidas, como a `Média de Close`, e para cálculos de variações e agregações.
* **Recursos de Inteligência Artificial**: Exploração da funcionalidade de **Narrativa Inteligente** para gerar explicações automáticas e contextuais sobre os dados do dashboard.
* **Filtros Interativos**: Implementação de filtros por `Empresa` e `Mês` para permitir análises dinâmicas e personalizadas.

---