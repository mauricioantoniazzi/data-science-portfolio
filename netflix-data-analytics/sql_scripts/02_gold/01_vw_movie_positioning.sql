CREATE OR ALTER VIEW vw_movie_positioning AS
SELECT 
    m.movieId,
    m.title_clean AS title,
    m.genres,
    rv.total_consumo,
    rv.media_nota,
    CASE 
        WHEN rv.total_consumo > 1000 AND rv.media_nota >= 3.8 THEN 'Blockbuster / Lenda'
        WHEN rv.total_consumo > 1000 AND rv.media_nota < 3.8 THEN 'Muito Popular'
        WHEN rv.total_consumo <= 1000 AND rv.media_nota >= 4.0 THEN 'Nicho / Cult'
        ELSE 'Popular'
    END AS categoria_sucesso
FROM dbo.tbl_movies_fixed m
JOIN vw_rating_vs_consumption rv ON m.movieId = rv.movieId;