{{ config(materialized='view') }}

-- Usando o delta_scan para ler os arquivos que o Spark criou
SELECT * FROM delta_scan('../data/silver/vendas_enriquecidas')