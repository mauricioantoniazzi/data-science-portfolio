# 📊 Análise de Dados de Logística com Power BI

Este projeto é um dashboard de **Análise de Dados de Logística**, criado no **Power BI Desktop**, com o objetivo de fornecer uma visão estratégica e completa sobre a eficiência do processo de entrega de produtos de uma empresa. O painel foi desenvolvido para corrigir e aprimorar um trabalho inicial que apresentava problemas de análise e visualização.

**Este projeto foi desenvolvido como parte de um estudo prático do curso do site [Data Science Academy](https://www.datascienceacademy.com.br/), focado em Business Intelligence e Análise de Dados.**

---

### 🎯 Objetivo do Projeto

O objetivo principal deste dashboard é transformar dados de entrega em **métricas-chave de desempenho (KPIs)** que suportam a tomada de decisões estratégicas. O painel foi reconstruído para responder a perguntas de negócio essenciais, como:

* **Qual o total de entregas no prazo por canal de entrega?**
* **Qual o percentual de entregas antecipadas por equipe?**
* **Como o volume de entregas varia ao longo do tempo (por mês)?**
* **Qual o total de entregas dos principais vendedores?**
* **Quais cidades têm o maior número de entregas com atraso?**
* **Qual a distribuição percentual das entregas por status (antecipado, no prazo, atrasado)?**

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`Logistica`) que contém informações detalhadas sobre os pedidos e entregas. As principais colunas da base de dados são:

* **Identificação**: `ID_Pedido`, `ID_Cliente`, `ID_Vendedor`, `ID_Cidade`
* **Tempo**: `Data_Pedido`, `Data_Entrega_Prevista`, `Data_Entrega_Realizada`
* **Logística**: `Canal_Entrega`, `Equipe_Entrega`, `Status_Entrega`
* **Medidas**: Medidas DAX foram criadas para calcular métricas como `Rating`, `Total Entregas`, `TotalEntregasPrazo`.

---

### ✨ Métricas e Análises Principais

O dashboard oferece uma visão abrangente sobre o processo de logística, com as seguintes métricas e análises:

* **Visão Geral**: Apresenta os cartões de indicadores com as métricas mais importantes, como **Total de Entregas** e **Total de Entregas no Prazo**.
* **Eficiência dos Canais**: Um gráfico de linha mostra o **Total de Entregas no Prazo por Canal de Entrega** para identificar os canais mais eficientes.
* **Desempenho por Equipe**: Um gráfico de barras exibe o **Percentual de Entregas por Equipe de Entrega**, permitindo avaliar o desempenho de cada equipe.
* **Volume de Entregas ao Longo do Tempo**: Um gráfico de linha mostra o **Total de Entregas por Mês**, ajudando a identificar tendências sazonais ou picos de demanda.
* **Distribuição de Status**: Um gráfico de barras exibe o **Percentual de Entregas Por Status de Entrega**, indicando a proporção de entregas antecipadas, no prazo e atrasadas.
* **Outras Análises**: A análise também inclui uma tabela com o **Total de Entregas de Produtos dos Top 5 Vendedores** e uma tabela com o **Total de Entregas com Atraso Por Cidade**.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **Power Query**: Utilizado para carregar e realizar transformações e limpezas nos dados.
* **DAX (Data Analysis Expressions)**: Usado para criar **medidas-chave de negócio**, como `Total Entregas` e `TotalEntregasPrazo`, que foram fundamentais para a análise e para o cálculo dos KPIs.

---