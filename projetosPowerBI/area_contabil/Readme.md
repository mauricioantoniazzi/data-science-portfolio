# 📊 Análise de Dados Contábeis: Balanço Patrimonial no Power BI

Este projeto é um dashboard focado em **Análise Contábil**, desenvolvido no **Power BI Desktop**, com o objetivo principal de representar um **Balanço Patrimonial dinâmico** e explorável. O foco está em demonstrar a capacidade do Power BI para trabalhar com dados financeiros estruturados e aprimorar a visualização de relatórios contábeis clássicos.

---

### 🎯 Objetivo do Projeto

O objetivo central deste projeto é simular e visualizar um Balanço Patrimonial de forma interativa no Power BI. Isso inclui:

* **Organizar e apresentar dados contábeis** de forma clara e hierárquica.
* **Utilizar o visual de Matriz** para exibir o Balanço Patrimonial com expansão e contração de níveis.
* **Permitir a análise da evolução dos valores** do Balanço Patrimonial ao longo dos anos.
* **Destacar o potencial do Power BI** para aprimorar relatórios financeiros tradicionais.

---

### 💾 Modelo de Dados e Fonte

O projeto utiliza um modelo de dados simples, mas eficaz, composto por duas tabelas conectadas:

1.  **`DadosContabeis`**: Contém os valores financeiros por ano e `ID_Conta`.
    * `Ano_2019`
    * `Ano_2020`
    * `Ano_2021`
    * `Ano_2022`
    * `Ano_2023`
    * `ID_Conta`
2.  **`PlanoContas`**: Atua como uma tabela de dimensão para estruturar o Balanço Patrimonial, fornecendo a hierarquia e o tipo de cada conta.
    * `Conta Nível 1`
    * `Conta Nível 2`
    * `Conta Nível 3`
    * `Conta Nível 4`
    * `ID_Conta`
    * `Tipo Relatório`

**Relacionamento**: As duas tabelas estão conectadas pelo campo `ID_Conta` em um relacionamento de **um para um**, garantindo que os dados contábeis sejam corretamente associados à sua hierarquia no plano de contas.

---

### ✨ Análises e Visualizações Principais

O dashboard é centrado em uma visualização principal que simula o Balanço Patrimonial:

* **Balanço Patrimonial Interativo (Visual de Matriz)**:
    * Apresenta uma visão hierárquica dos ativos e passivos da empresa, permitindo a expansão e contração dos níveis (`Conta Nível 1` até `Conta Nível 4`).
    * Exibe os valores contábeis para cada ano (`2019` a `2023`), facilitando a análise da evolução financeira.
    * Utiliza formatação condicional para destacar visualmente a variação dos valores.

---

### 🛠️ Tecnologias e Recursos Utilizados

* **Power BI Desktop**: Ferramenta principal para modelagem de dados, criação de medidas e desenvolvimento do dashboard.
* **Power Query**: Utilizado para carregar e, se necessário, realizar transformações e limpezas iniciais nas fontes de dados.
* **Modelagem de Dados**: Estruturação do relacionamento entre as tabelas `DadosContabeis` e `PlanoContas` para criar uma hierarquia eficiente.
* **DAX (Data Analysis Expressions)**: Usado para criar medidas implícitas (soma dos anos) e formatar o visual, garantindo a agregação correta dos valores.
* **Visual de Matriz**: Exploração avançada das funcionalidades do visual de Matriz para criar um Balanço Patrimonial hierárquico e interativo.

---