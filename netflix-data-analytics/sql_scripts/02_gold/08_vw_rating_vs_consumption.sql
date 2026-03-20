CREATE OR ALTER VIEW vw_rating_vs_consumption AS
SELECT 
    m.movieId,
    m.title_clean AS title,
    m.genres,
    m.release_year,
    -- Eixo X: Consumo (Total de avaliações na base unificada)
    COUNT(r.userId) AS total_consumo,
    -- Eixo Y: Qualidade (Média das notas)
    ROUND(AVG(CAST(r.rating AS FLOAT)), 2) AS media_nota,
    -- "Polêmica": Desvio Padrão das notas
    ROUND(STDEV(CAST(r.rating AS FLOAT)), 2) AS desvio_padrao_nota
FROM tbl_movies_fixed m
INNER JOIN tbl_ratings_fixed r ON m.movieId = r.movieId
GROUP BY m.movieId, m.title_clean, m.genres, m.release_year;