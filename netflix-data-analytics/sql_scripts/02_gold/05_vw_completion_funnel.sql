CREATE OR ALTER VIEW vw_completion_funnel AS
WITH aggregated_ratings AS (
    SELECT userId, movieId, 1 AS finished
    FROM vw_all_ratings_unified
    GROUP BY userId, movieId
),
user_context AS (
    SELECT 
        b.movieId,
        b.userId,
        m.genres, 
        CASE WHEN b.isSeen = 1 THEN 1 ELSE 0 END AS started,
        ISNULL(r.finished, 0) AS finished
    FROM dbo.belief_data b
    INNER JOIN dbo.tbl_movies_fixed m ON b.movieId = m.movieId
    LEFT JOIN aggregated_ratings r ON b.userId = r.userId AND b.movieId = r.movieId
)
SELECT 
    movieId,
    genres,
    COUNT(userId) AS total_interacted,
    SUM(started) AS total_started,
    SUM(finished) AS total_finished
FROM user_context
GROUP BY movieId, genres;