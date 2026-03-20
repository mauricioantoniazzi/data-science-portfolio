CREATE OR ALTER VIEW vw_funnel_unpivoted AS
SELECT genres, '1. Interacted' AS step, SUM(total_interacted) AS total_value 
FROM vw_completion_funnel
GROUP BY genres
UNION ALL
SELECT genres, '2. Started' AS step, SUM(total_started) AS total_value 
FROM vw_completion_funnel
GROUP BY genres
UNION ALL
SELECT genres, '3. Finished' AS step, SUM(total_finished) AS total_value 
FROM vw_completion_funnel
GROUP BY genres;