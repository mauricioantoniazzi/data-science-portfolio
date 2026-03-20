-- Criando a tabela física de filmes com os nomes e anos já limpos
SELECT 
    movieId,
    -- Lógica de limpeza que validamos antes
    LTRIM(RTRIM(
        CASE 
            WHEN LEN(title) > 7 AND title LIKE '%([0-9][0-9][0-9][0-9])' 
            THEN LEFT(title, LEN(title) - 7) 
            ELSE title 
        END
    )) AS title_clean,
    TRY_CAST(
        CASE 
            WHEN LEN(title) > 7 AND title LIKE '%([0-9][0-9][0-9][0-9])' 
            THEN SUBSTRING(title, LEN(title) - 4, 4) 
            ELSE NULL 
        END AS INT
    ) AS release_year,
    genres
INTO tbl_movies_fixed
FROM movies;

-- Criar um índice para o JOIN não travar
CREATE CLUSTERED INDEX idx_movies_fixed_id ON tbl_movies_fixed (movieId);