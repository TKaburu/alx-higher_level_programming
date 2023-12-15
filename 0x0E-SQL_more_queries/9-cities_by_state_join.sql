-- List cities in hbtn_0d_usa
-- Each should display cities.id - cities.name - states.name
-- Result should be  sorted in ascending order

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
