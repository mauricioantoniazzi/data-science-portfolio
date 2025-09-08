# 📊 Análise de Dados Financeiros com Power BI

Este projeto é um dashboard de **Análise Financeira**, criado no **Power BI Desktop**, com o objetivo de fornecer uma visão clara e estratégica sobre as receitas, despesas e a lucratividade da empresa.

---

### 🎯 Objetivo do Projeto

O objetivo principal deste dashboard é transformar dados financeiros em **indicadores-chave de desempenho (KPIs)** para que os tomadores de decisão possam monitorar a saúde financeira da empresa. O painel foi construído para responder a perguntas de negócio essenciais, como:

* **Qual a margem de lucro atual da empresa?**
* **Quais são os principais componentes de receita e despesa?**
* **Como receitas e despesas se comportam ao longo do tempo?**
* **Quais segmentos de negócio geram mais receita e despesa?**

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`DadosFinanceiros`) que contém informações detalhadas sobre as transações financeiras da empresa. As principais colunas da base de dados são:

* **Dados**: `Valor`
* **Tempo**: `Data`
* **Categorias**: `Tipo` e `Componente`

Medidas DAX foram criadas para calcular métricas financeiras cruciais:

* `Lucro`
* `MargemLucro`
* `TotalDespesas`
* `TotalReceitas`

---

### ✨ Métricas e Análises Principais

O dashboard oferece uma visão abrangente sobre o desempenho financeiro, com as seguintes métricas e análises:

* **Visão Geral**: Apresenta os cartões de indicadores com as métricas mais importantes, como o **Total de Receitas**, **Total de Despesas** e a **Margem de Lucro**.
* **Distribuição de Receitas e Despesas**: Gráficos que mostram o **Total de Receitas Por Componente** e o **Total de Despesas Por Componente** em relação à média, permitindo identificar as áreas de maior impacto.
* **Análise por Tempo e Componente**: Uma tabela que exibe o **Total de Receitas e Despesas por Componente e por Ano**, com a hierarquia `Tipo`/`Componente` para uma análise detalhada.
* **Análise de Segmentos**: O dashboard permite identificar os segmentos de negócio onde as receitas e despesas são maiores ou menores, fornecendo insights estratégicos para o planejamento.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **DAX (Data Analysis Expressions)**: Usado extensivamente para criar as **medidas financeiras-chave**, como `Total de Receitas`, `Total de Despesas` e `Margem de Lucro`, que foram fundamentais para a análise e o cálculo dos KPIs.

---