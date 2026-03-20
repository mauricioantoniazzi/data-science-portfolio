CREATE OR ALTER VIEW vw_rating_evolution AS
SELECT 
    CAST(tstamp AS DATE) AS data_avaliacao,
    YEAR(tstamp) AS ano_avaliacao,
    MONTH(tstamp) AS mes_avaliacao,
    COUNT(movieId) AS qtd_avaliacoes,
    AVG(CAST(rating AS FLOAT)) AS media_periodo
FROM dbo.tbl_ratings_fixed
GROUP BY CAST(tstamp AS DATE), YEAR(tstamp), MONTH(tstamp);