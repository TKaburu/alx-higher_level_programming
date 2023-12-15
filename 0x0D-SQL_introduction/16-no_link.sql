-- List all records of second_table. It should display score and name
-- Order by score descending

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
