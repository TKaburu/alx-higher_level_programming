-- Lists all cities of California that can be found in hbtn_0d_usa
-- Results must be in ascending order by cities.id

USE hbtn_0d_usa;

SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
