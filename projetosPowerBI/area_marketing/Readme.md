# 📊 Análise de Campanhas de Marketing com Power BI

Este projeto é um mini-dashboard de análise de marketing, desenvolvido no **Power BI Desktop**, com o objetivo de fornecer uma visão completa do perfil do cliente, seus hábitos de compra e a efetividade das campanhas de marketing.

**Este mini-projeto foi desenvolvido como parte de um estudo prático do curso do site [Data Science Academy](https://www.datascienceacademy.com.br/), focado em Business Intelligence e Análise de Dados.**

---

### 🎯 Objetivo do Projeto

O objetivo principal é transformar dados brutos de marketing em **insights acionáveis**, dividindo a análise em quatro visões estratégicas para facilitar a tomada de decisão:

* **Visão do Cliente**
* **Visão do Comportamento de Compra do Cliente**
* **Visão da Performance das Campanhas de Marketing**
* **Visão dos Padrões de Compra por Ponto de Venda (País)**

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`DadosMarketing`) que contém informações detalhadas sobre os clientes, seus gastos e a interação com campanhas promocionais. As principais colunas da base de dados são:

* **Informações Pessoais**: `Escolaridade`, `Estado Civil`, `Anos em Casa` e `Filhos em Casa`.
* **Dados de Gastos**: `Salário Anual` e gastos com diferentes categorias de produtos (`Móveis`, `Utensílios`, `Vestuário`, `Alimentos`, `Eletrônicos` e `Brinquedos`).
* **Comportamento de Compra**: `Número de Compras` por canal (web, loja, catálogo), `Número de Visitas ao Website` e `Número de Compras com Desconto`.
* **Campanhas**: Status de compra (`Sim`/`Não`) nas campanhas de `1` a `5`.

---

### ✨ Análises e Visualizações Principais

Cada uma das quatro visões do dashboard oferece uma perspectiva única e valiosa sobre o negócio:

1.  **Visão do Cliente**: Apresenta um panorama geral da base de clientes, com métricas como o **Total de Clientes**, **Salário Anual Médio** e o número de compras por diferentes canais.
2.  **Visão do Comportamento**: Explora o comportamento de compra do cliente, analisando o **gasto total por perfil** (`Estado Civil` e `Escolaridade`) e como o gasto se relaciona com o **Salário Anual**, `Filhos em Casa` e `Adolescentes em Casa`.
3.  **Visão de Campanhas**: Avalia a **efetividade das campanhas de marketing** ao cruzar o resultado (`comprou` ou `não comprou`) com o `Número de Filhos` e o **Salário Anual**, além de exibir a proporção geral de sucesso das campanhas.
4.  **Visão Pontos de Venda**: Analisa os **padrões de compra por país**, mostrando o gasto total em diferentes categorias e a evolução do gasto ao longo do tempo por cada país.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **Power Query**: Utilizado para carregar e realizar transformações e limpezas simples nos dados.
* **DAX (Data Analysis Expressions)**: Usado para criar medidas e agregar informações, como `TotalGasto`, para as análises.

---