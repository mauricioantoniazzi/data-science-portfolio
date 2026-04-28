-- Este modelo limpa e renomeia os dados brutos da v4
SELECT
    CAST(moeda AS VARCHAR) as codigo_moeda,
    CAST(valor AS DECIMAL(18,4)) as preco_fechamento,
    CAST(data_cotacao AS TIMESTAMP) as data_referencia,
    processado_em
FROM {{ source('cotacao_raw', 'staging_cotacoes') }}