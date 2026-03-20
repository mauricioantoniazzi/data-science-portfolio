CREATE OR ALTER VIEW vw_recommendation_efficiency AS
SELECT 
    b.movieId,
    m.title_clean AS title,
    m.genres,
    -- Total de vezes que este filme apareceu como recomendação/crença
    COUNT(b.userId) AS total_opportunities,
    -- Total de vezes que o usuário realmente deu PLAY (isSeen = 1)
    SUM(CASE WHEN b.isSeen = 1 THEN 1 ELSE 0 END) AS total_hits,
    -- Taxa de Conversão de Recomendação (%)
    ROUND(
        (CAST(SUM(CASE WHEN b.isSeen = 1 THEN 1 ELSE 0 END) AS FLOAT) / 
        NULLIF(COUNT(b.userId), 0)) * 100, 2
    ) AS conversion_rate_pct
FROM tbl_belief_fixed b
INNER JOIN tbl_movies_fixed m ON b.movieId = m.movieId
GROUP BY b.movieId, m.title_clean, m.genres;