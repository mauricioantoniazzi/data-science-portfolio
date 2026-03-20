CREATE OR ALTER VIEW vw_movie_performance AS
WITH movie_cleaned AS (
    SELECT 
        movieId,
        -- Só tenta cortar se o título for longo o suficiente e terminar com o padrão (YYYY)
        LTRIM(RTRIM(
            CASE 
                WHEN LEN(title) > 7 AND title LIKE '%([0-9][0-9][0-9][0-9])' 
                THEN LEFT(title, LEN(title) - 7) 
                ELSE title 
            END
        )) AS title_clean,
        
        -- Extrai o ano apenas se o padrão for detectado no final
        TRY_CAST(
            CASE 
                WHEN LEN(title) > 7 AND title LIKE '%([0-9][0-9][0-9][0-9])' 
                THEN SUBSTRING(title, LEN(title) - 4, 4) 
                ELSE NULL 
            END AS INT
        ) AS release_year,
        genres
    FROM movies
),
movie_stats AS (
    SELECT 
        movieId,
        COUNT(userId) AS total_engagements,
        AVG(CAST(rating AS FLOAT)) AS avg_rating
    FROM user_rating_history
    GROUP BY movieId
)
SELECT 
    m.movieId,
    m.title_clean AS title,
    m.release_year,
    m.genres,
    ISNULL(s.total_engagements, 0) AS total_engagements,
    ROUND(ISNULL(s.avg_rating, 0), 2) AS avg_rating
FROM movie_cleaned m
LEFT JOIN movie_stats s ON m.movieId = s.movieId;