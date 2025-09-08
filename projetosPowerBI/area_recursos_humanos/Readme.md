# 📊 Análise de Dados de RH com Power BI

Este projeto é um dashboard de **Análise de Dados de Recursos Humanos**, criado no **Power BI Desktop**, com o objetivo de fornecer uma visão estratégica e completa sobre a força de trabalho da empresa.

**Este projeto foi desenvolvido como parte de um estudo prático do curso do site [Data Science Academy](https://www.datascienceacademy.com.br/), focado em Business Intelligence e Análise de Dados.**

---

### 🎯 Objetivo do Projeto

O objetivo principal deste dashboard é transformar dados brutos de RH em **métricas-chave** que suportam a tomada de decisões estratégicas. O painel foi construído para responder a perguntas de negócio essenciais, como:

* **Qual o total de funcionários, divididos por gênero?**
* **Qual o salário médio e o tempo médio de experiência na empresa?**
* **Como está a distribuição de funcionários por função?**
* **Qual o nível de envolvimento dos funcionários com o trabalho?**
* **Qual o percentual de funcionários aptos a receber hora extra?**

---

### 💾 Fonte de Dados

A análise foi realizada a partir de uma base de dados fictícia (`dadosRH`) que contém informações detalhadas sobre a equipe de funcionários. As principais colunas da base de dados são:

* **Identificação**: `Id_Funcionario`
* **Dados Pessoais**: `Idade`, `Genero`, `Estado Civil`
* **Dados Profissionais**: `Anos_Experiencia`, `Anos_na_Empresa`, `Funcao`, `Salario_Mensal`, `Aval_Performance`
* **Engajamento e Promoção**: `Envolvimento_Trabalho`, `Nivel_Satisfacao_Trabalho`, `Anos_Desde_Ultima_Promocao`, `StatusPromo`

---

### ✨ Métricas e Análises Principais

O dashboard oferece uma visão abrangente sobre o capital humano da empresa, com as seguintes métricas e análises:

* **Visão Geral**: Apresenta os cartões de indicadores com as métricas mais importantes, como **Total de Funcionários**, **Salário Médio** e **Experiência Média**.
* **Diversidade**: Mostra a distribuição do quadro de funcionários por **Gênero**, com o total e o percentual de funcionários masculinos e femininos.
* **Distribuição por Função**: Um gráfico de barras que exibe o **Total de Funcionários Por Função**, facilitando a visualização da estrutura organizacional.
* **Engajamento**: Um gráfico de rosca que avalia o nível de **Envolvimento no Trabalho** dos funcionários, segmentado em categorias como Ruim, Baixo, Médio e Alto.
* **Disponibilidade para Horas Extras**: Um gráfico de pizza que mostra o percentual de funcionários disponíveis para realizar horas extras.
* **Análise de Promoção**: Uma análise que não está no dashboard, mas que foi calculada, identificando o **Total e o Percentual de Funcionários que devem ser considerados para promoção**, com base na regra de ter **5 anos ou mais desde a última promoção**.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para a criação do projeto.
* **Power Query**: Utilizado para carregar e realizar transformações e limpezas nos dados.
* **DAX (Data Analysis Expressions)**: Amplamente utilizado para criar **medidas complexas**, como `SalarioMedio`, `TotalFunc`, `% Masculino` e `TotalFuncPromover`, que foram essenciais para responder às perguntas de negócio.

---