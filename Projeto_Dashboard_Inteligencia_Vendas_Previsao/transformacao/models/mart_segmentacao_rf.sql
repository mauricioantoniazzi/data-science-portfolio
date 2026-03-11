-- Pergunta: "Quem são meus clientes 'em risco' e quem são os 'campeões'?"
-- Objetivo: Identificar clientes que estão parando de comprar (em risco) e os que são fiéis (campeões).

{{ config(materialized='table') }}

WITH base_clientes AS (
  -- Passo 1 e 2: Capturar a última compra e total de pedidos por cliente
	SELECT
		Nome_Cliente,
		MAX(Data_Venda) as data_ultima_compra,
		COUNT(DISTINCT ID_Pedido) as total_pedidos,
		SUM(Valor_Total) as faturamento_historico
	FROM {{ ref('fct_vendas_indicadores') }}
	GROUP BY Nome_Cliente
),

calculo_dias AS (
	-- Passo 3: Calcular a Recência em dias
  -- Usamos a data máxima do banco para simular o "hoje" ou GETDATE()
	SELECT
		*,
		DATEDIFF(day, data_ultima_compra, (SELECT MAX(Data_Venda) FROM {{ ref('fct_vendas_indicadores') }})) as dias_sem_comprar
	FROM base_clientes
)

-- Passo 4: Classificação de Negócio
SELECT
	*,
	CASE
		WHEN dias_sem_comprar <= 30 AND total_pedidos >=5 THEN 'Campeão (Fiel)'
		WHEN dias_sem_comprar <= 30 AND total_pedidos < 5 THEN 'Novo Cliente'
		WHEN dias_sem_comprar > 90 AND total_pedidos >= 5 THEN 'Em Risco (Recuperar)'
		WHEN dias_sem_comprar > 180 THEN 'Hibernando / Perdido'
		ELSE 'Potencial a desenvolver'
	END as status_cliente
FROM calculo_dias