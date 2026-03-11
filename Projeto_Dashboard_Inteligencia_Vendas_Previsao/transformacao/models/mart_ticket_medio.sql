-- Qual o Ticket Médio por Categoria e Canal?
-- Objetivo: Entender onde o cliente gasta mais por transação.

{{ config(materialized='table') }}

SELECT
  CATEGORIA,
  DESCRICAO_CANAL,
  COUNT(ID_PEDIDO) AS total_pedidos,
  SUM(VALOR_TOTAL) AS faturamento_total,
  SUM(VALOR_TOTAL) / COUNT(ID_PEDIDO) AS ticket_medio
FROM {{ ref('fct_vendas_indicadores') }}
GROUP BY
  CATEGORIA,
  DESCRICAO_CANAL