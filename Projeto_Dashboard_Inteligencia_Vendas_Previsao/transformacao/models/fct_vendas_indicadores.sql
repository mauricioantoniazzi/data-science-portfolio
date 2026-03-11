{{ config(materialized='table') }}

WITH base_venda AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Venda') }}
),
base_produto AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Produto') }}
),
base_marca AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Marca') }}
),
base_subcategoria AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Subcategoria') }}
),
base_categoria AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Categoria') }}
),
base_cliente AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Cliente') }}
),
base_cidade AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Cidade') }}
),
base_canal AS (
    SELECT * FROM {{ source('sql_server_vendas', 'Canal') }}
)

SELECT
    V.ID_Pedido,
    V.Data_Venda,
    V.Data_Entrega,
    V.Qtde,
    V.Valor_Total,
    P.Descricao_Produto,
    P.Custo,
    P.Preco_Unitario,
    P.Tributos,
    M.Marca,
    C.Categoria,
    SC.Subcategoria,
    CL.Nome AS Nome_Cliente,
    CL.Genero,
    CD.Cidade,
    CD.UF,
    CA.Descricao_Canal
FROM 
    base_venda V
JOIN base_produto P ON V.ID_Produto = P.ID_Produto
JOIN base_marca M ON P.ID_Marca = M.ID_Marca
JOIN base_subcategoria SC ON P.ID_Subcategoria = SC.ID_Subcategoria
JOIN base_categoria C ON SC.ID_Categoria = C.ID_Categoria
JOIN base_cliente CL ON V.ID_Cliente = CL.ID_Cliente
JOIN base_cidade CD ON CL.ID_Cidade = CD.ID_Cidade
JOIN base_canal CA ON V.ID_Canal = CA.ID_Canal