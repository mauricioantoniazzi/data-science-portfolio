CREATE OR ALTER VIEW vw_recommendation_accuracy AS
SELECT 
    b.movieId,
    m.title_clean AS title,
    m.genres,
    -- Média do que o sistema previu para este filme
    AVG(b.systemPredictRating) AS avg_system_predicted,
    -- Média do que os usuários realmente deram
    AVG(r.rating) AS avg_user_actual,
    -- Cálculo do Erro Médio Absoluto (MAE)
    AVG(ABS(b.systemPredictRating - r.rating)) AS mean_absolute_error,
    -- Volume de recomendações testadas
    COUNT(r.userId) AS sample_size
FROM dbo.belief_data b -- Usando a base original de belief para pegar o systemPredictRating
INNER JOIN tbl_ratings_fixed r 
    ON b.userId = r.userId 
    AND b.movieId = r.movieId
INNER JOIN tbl_movies_fixed m 
    ON b.movieId = m.movieId
WHERE b.systemPredictRating IS NOT NULL
GROUP BY b.movieId, m.title_clean, m.genres;