{{ config(materialized='table') }}

SELECT
    md5(codigo_moeda || data_referencia) as sk_cotacao, -- Surrogate Key
    md5(codigo_moeda) as fk_moeda, -- Chave estrangeira para a Dimensão
    preco_fechamento,
    data_referencia
FROM {{ ref('stg_cotacoes') }}
WHERE preco_fechamento > 0