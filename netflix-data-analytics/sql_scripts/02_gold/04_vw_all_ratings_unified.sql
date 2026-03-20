CREATE OR ALTER VIEW vw_all_ratings_unified AS
SELECT userId, movieId, rating, tstamp FROM user_rating_history
UNION ALL
SELECT userId, movieId, rating, tstamp FROM ratings_for_additional_users;