-- Criando uma tabela unificada de Ratings (Já limpa e indexada)
SELECT 
    CAST(userId AS VARCHAR(50)) AS userId, 
    CAST(movieId AS INT) AS movieId, 
    CAST(rating AS FLOAT) AS rating, 
    tstamp
INTO tbl_ratings_fixed
FROM (
    SELECT userId, movieId, rating, tstamp FROM user_rating_history
    UNION ALL
    SELECT userId, movieId, rating, tstamp FROM ratings_for_additional_users
) AS raw;
