-- Quais são os Produtos com Melhor Margem (Preço vs Custo)?
-- Objetivo: Identificar os produtos que trazem mais lucro real, não apenas faturamento

{{ config(materialized='table') }}

SELECT 
    Descricao_Produto,
    Marca,
    SUM(Valor_Total) as faturamento_total,
    SUM(Custo * Qtde) as custo_total,
    SUM(Valor_Total) - SUM(Custo * Qtde) as lucro_estimado,
    ((SUM(Valor_Total) - SUM(Custo * Qtde)) / NULLIF(SUM(Valor_Total), 0)) * 100 as margem_percentual
FROM {{ ref('fct_vendas_indicadores') }}
GROUP BY Descricao_Produto, Marca