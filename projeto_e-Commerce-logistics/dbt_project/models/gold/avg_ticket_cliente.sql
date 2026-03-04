SELECT 
    cliente_id,
    AVG(valor) as ticket_medio
FROM {{ ref('stg_vendas') }}
GROUP BY 1