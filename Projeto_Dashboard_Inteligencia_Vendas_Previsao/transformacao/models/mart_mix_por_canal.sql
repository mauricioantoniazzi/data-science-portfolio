{{ config(materialized='table') }}

WITH metricas_por_canal AS (
    -- Consolidar vendas por Canal e Categoria
    SELECT 
        Descricao_Canal,
        Categoria,
        COUNT(ID_Pedido) as qtd_pedidos,
        SUM(Valor_Total) as faturamento_canal_cat,
        AVG(Valor_Total) as ticket_medio_canal_cat
    FROM {{ ref('fct_vendas_indicadores') }}
    GROUP BY Descricao_Canal, Categoria
),

total_canal AS (
    -- Calcular o faturamento total de cada canal para achar a proporção
    SELECT 
        *,
        SUM(faturamento_canal_cat) OVER (PARTITION BY Descricao_Canal) as faturamento_total_do_canal
    FROM metricas_por_canal
)

-- Resultado Final com a % de representatividade
SELECT 
    *,
    (faturamento_canal_cat / faturamento_total_do_canal) * 100 as pct_representatividade_no_canal
FROM total_canal