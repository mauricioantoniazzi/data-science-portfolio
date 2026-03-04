{{ config(materialized='table') }}

WITH base_vendas AS (
    SELECT * FROM {{ ref('stg_vendas') }}
)

SELECT 
    categoria,
    ano,
    mes,
    ROUND(SUM(valor), 2) as receita_total,
    COUNT(pedido_id) as qtd_pedidos
FROM base_vendas
GROUP BY 1, 2, 3
ORDER BY ano DESC, mes DESC, receita_total DESC