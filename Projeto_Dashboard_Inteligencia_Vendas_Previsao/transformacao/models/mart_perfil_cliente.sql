-- Qual a Performance de Vendas por Gênero e Região?
-- Objetivo: Ajustar campanhas de marketing geográficas e demográficas.

{{ config(materialized='table') }}

SELECT 
    UF,
    Genero,
    SUM(Qtde) as total_itens,
    SUM(Valor_Total) as faturamento,
    COUNT(DISTINCT Nome_Cliente) as base_clientes_ativos
FROM {{ ref('fct_vendas_indicadores') }}
GROUP BY UF, Genero