CREATE OR ALTER VIEW vw_metabase_movie_master AS
SELECT 
    m.movieId,
    ISNULL(m.title_clean, 'Título Desconhecido') AS title,
    ISNULL(m.release_year, 0) AS release_year,
    ISNULL(m.genres, 'Não Categorizado') AS genres,
    
    -- Tratando contagens nulas como 0
    ISNULL(f.total_interacted, 0) AS total_interacted,
    ISNULL(f.total_started, 0) AS total_started,
    ISNULL(f.total_finished, 0) AS total_finished,
    
    -- Tratando métricas de avaliação
    ISNULL(rv.media_nota, 0) AS media_nota,
    ISNULL(rv.total_consumo, 0) AS total_consumo,
    
    -- Tratando as taxas para evitar divisões por zero ou nulos
    ROUND(ISNULL(CAST(f.total_finished AS FLOAT) / NULLIF(f.total_started, 0), 0), 4) AS completion_rate,
    ROUND(ISNULL(CAST(f.total_started AS FLOAT) / NULLIF(f.total_interacted, 0), 0), 4) AS attraction_rate
FROM tbl_movies_fixed m
LEFT JOIN vw_completion_funnel f ON m.movieId = f.movieId
LEFT JOIN vw_rating_vs_consumption rv ON m.movieId = rv.movieId;