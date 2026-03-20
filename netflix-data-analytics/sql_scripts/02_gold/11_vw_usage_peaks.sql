CREATE OR ALTER VIEW vw_usage_peaks AS
WITH time_data AS (
    SELECT 
        r.movieId,
        m.genres, -- <--- Trouxemos o gênero para o cálculo
        CAST(r.tstamp AS DATETIME) AS dt_click
    FROM tbl_ratings_fixed r
    INNER JOIN dbo.movies m ON r.movieId = m.movieId -- <--- Join necessário para o filtro
)
SELECT 
    genres, -- <--- Adicionado ao agrupamento
    dia_semana_num = DATEPART(WEEKDAY, dt_click),
    dia_semana_nome = DATENAME(WEEKDAY, dt_click),
    hora_dia = DATEPART(HOUR, dt_click),
    total_acessos = COUNT(*)
FROM time_data
GROUP BY 
    genres,
    DATEPART(WEEKDAY, dt_click), 
    DATENAME(WEEKDAY, dt_click), 
    DATEPART(HOUR, dt_click);