-- Quais produtos representam 80% do meu faturamento?
/*
  Negócio: Em quase toda empresa, uma minoria de produtos (Classe A) gera a maioria da receita.
  Identificá-los serve para:
     - Nunca deixar faltar estoque desses itens.
     - Negociar preços melhores com os fornecedores desses produtos específicos.
     - Não gastar energia excessiva com produtos "cauda longa" que vendem pouco.
*/

{{ config(materialized='table') }}

WITH faturamento_por_produto AS (
    -- Passo 1: Agregação por produto
    SELECT 
        Descricao_Produto,
        Categoria,
        SUM(Valor_Total) as faturamento_item
    FROM {{ ref('fct_vendas_indicadores') }}
    GROUP BY Descricao_Produto, Categoria
),

calculo_acumulado AS (
    -- Passo 2 e 3: Ordenação e Soma Acumulada
    /*
    Faturamento Acumulado: Aqui entra o cálculo de "Janela" (Window Function).
    na linha do 2º produto, o SQL some o faturamento dele com o do 1º.
    Na linha do 3º, some com os dois anteriores, e assim por diante.
    */
    SELECT 
        *,
        SUM(faturamento_item) OVER (ORDER BY faturamento_item DESC) as faturamento_acumulado,
        SUM(faturamento_item) OVER () as faturamento_total_empresa
    FROM faturamento_por_produto
),

percentuais AS (
    -- Passo 4: Transformar em porcentagem
    SELECT 
        *,
        (faturamento_acumulado / faturamento_total_empresa) * 100 as pct_acumulado
    FROM calculo_acumulado
)

-- Passo 5: Classificação Final
SELECT 
    *,
    CASE 
        WHEN pct_acumulado <= 80 THEN 'A'
        WHEN pct_acumulado <= 95 THEN 'B'
        ELSE 'C'
    END as classificacao_abc
FROM percentuais
