{{ config(materialized='table') }}

WITH unique_moedas AS (
    SELECT DISTINCT
        codigo_moeda
    FROM {{ ref('stg_cotacoes') }}
)

SELECT
    md5(codigo_moeda) as sk_moeda, -- Surrogate Key da Dimensão
    codigo_moeda,
    CASE 
        WHEN codigo_moeda = 'USD' THEN 'Dólar Americano'
        WHEN codigo_moeda = 'EUR' THEN 'Euro'
        WHEN codigo_moeda = 'BRL' THEN 'Real Brasileiro'
        WHEN codigo_moeda = 'BTC' THEN 'Bitcoin'
        WHEN codigo_moeda = 'GBP' THEN 'Libra Esterlina'
        WHEN codigo_moeda = 'ARS' THEN 'Peso Argentino'
        ELSE 'Outras Moedas'
    END as nome_moeda
FROM unique_moedas