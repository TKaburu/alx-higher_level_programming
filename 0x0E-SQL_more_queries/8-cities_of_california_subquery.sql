-- Lists all cities of California that can be found in hbtn_0d_usa
-- Results must be in ascending order by cities.id

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'california'
)
ORDER BY id ASC;
