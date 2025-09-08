# 📊 Análise de Vendas - Dashboard de Desempenho

Este projeto é um dashboard interativo de análise de vendas, criado no **Power BI Desktop**, com o objetivo de transformar dados brutos em insights de negócio e identificar os principais fatores de influência nas vendas.

**Este projeto faz parte de um estudo prático do curso do site [Data Science Academy](https://www.datascienceacademy.com.br/), focado em Business Intelligence e Análise de Dados.**

---

### 🎯 Objetivo do Projeto

O objetivo principal deste dashboard é fornecer uma visão estratégica e responder a perguntas-chave como:

* **Quais produtos, segmentos e fabricantes impulsionam as vendas?**
* **Qual o desempenho de vendas por categoria, loja e vendedor?**
* **Quais fatores influenciam o aumento ou a diminuição do valor das vendas?**

---

### 💾 Fonte de Dados

Os dados utilizados são fictícios e foram fornecidos em uma única tabela, contendo informações sobre:

* **Vendas**: `ValorVenda`, `Custo`, `Comissão`
* **Tempo**: `Data Venda` (com dados de 2012 a 2015)
* **Produtos**: `Categoria`, `Segmento`, `Produto`, `Fabricantes`
* **Localização**: `Cidade`, `Estado`, `Loja`
* **Vendedores**: `Vendedor`

---

### ✨ Análises e Visualizações Principais

O dashboard é composto por diferentes visualizações que oferecem uma análise detalhada dos dados de vendas.

* **Narrativa Inteligente**: Fornece um resumo dinâmico das informações, destacando as maiores e menores participações por **Segmento**, **Fabricantes** e **Categoria**.
* **Gráfico de Faixas (Sankey)**: Mostra o fluxo de valor de vendas entre as **Categorias** e os **Pontos de Venda**, ajudando a visualizar as rotas de venda mais lucrativas.
* **Principais Influenciadores**: Usa a inteligência artificial do Power BI para identificar os fatores que mais influenciam o aumento da média de vendas.
* **Mapa**: Visualiza o **Total de Valor de Venda por Estado e Vendedor**, permitindo uma análise geoespacial do desempenho de vendas.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **Power Query**: Usado para carregar e realizar transformações e limpezas simples nos dados.
* **Recursos Avançados**: Foram exploradas funcionalidades de **Análise de IA** do Power BI, como a **Narrativa Inteligente** e os **Principais Influenciadores**.
* **Observação**: Neste primeiro projeto, o foco foi a exploração dos recursos de visualização e análise. O uso de **DAX** (Data Analysis Expressions) não foi necessário, demonstrando a capacidade da ferramenta de gerar insights poderosos mesmo sem o uso de código complexo.

---
