CREATE OR ALTER VIEW vw_user_segments AS
WITH user_counts AS (
    SELECT 
        userId, 
        COUNT(movieId) AS qtd_avaliacoes
    FROM dbo.tbl_ratings_fixed
    GROUP BY userId
)
SELECT 
    userId,
    qtd_avaliacoes,
    CASE 
        WHEN qtd_avaliacoes <= 100 THEN 'Casual'
        WHEN qtd_avaliacoes > 100 AND qtd_avaliacoes <= 1000 THEN 'Entusiasta'
        ELSE 'Super Crítico'
    END AS perfil_usuario
FROM user_counts;