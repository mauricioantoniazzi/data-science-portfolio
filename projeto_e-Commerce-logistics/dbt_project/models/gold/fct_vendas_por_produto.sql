{{ config(materialized='table') }}

WITH base_vendas AS (
    SELECT * FROM {{ ref('stg_vendas') }}
)

SELECT 
    nome_produto,
    ROUND(SUM(valor), 2) as receita_total,
FROM base_vendas
GROUP BY 1
ORDER BY receita_total DESC