-- Criando uma versão leve da belief_data
SELECT 
    CAST(userId AS VARCHAR(50)) AS userId, 
    CAST(movieId AS INT) AS movieId, 
    CAST(isSeen AS INT) AS isSeen
INTO tbl_belief_fixed
FROM dbo.belief_data;