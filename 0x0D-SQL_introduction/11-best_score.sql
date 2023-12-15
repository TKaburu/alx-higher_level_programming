-- lists all records with a score >= 10 in second_table ordered by score
-- Should display score and name

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
