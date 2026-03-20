CREATE OR ALTER VIEW vw_user_retention AS
WITH user_first_activity AS (
    -- Identifica quando o usuário entrou na plataforma (Primeira avaliação)
    SELECT 
        userId, 
        MIN(CAST(tstamp AS DATETIME)) AS first_access,
        FORMAT(MIN(CAST(tstamp AS DATETIME)), 'yyyy-MM') AS cohort_month
    FROM tbl_ratings_fixed
    GROUP BY userId
),
user_activity_months AS (
    -- Mapeia todos os meses em que o usuário foi ativo
    SELECT DISTINCT 
        userId, 
        FORMAT(CAST(tstamp AS DATETIME), 'yyyy-MM') AS activity_month
    FROM tbl_ratings_fixed
)
SELECT 
    f.cohort_month,
    a.activity_month,
    -- Diferença de meses entre o primeiro acesso e a atividade atual
    DATEDIFF(MONTH, CAST(f.cohort_month + '-01' AS DATE), CAST(a.activity_month + '-01' AS DATE)) AS month_number,
    COUNT(DISTINCT a.userId) AS active_users
FROM user_first_activity f
JOIN user_activity_months a ON f.userId = a.userId
GROUP BY f.cohort_month, a.activity_month;