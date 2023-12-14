-- Create id_not_null table with id and name descriptions
-- Set id default value to 1
-- If table already exists scrip should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
