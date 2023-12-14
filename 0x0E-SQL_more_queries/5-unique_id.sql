-- Create unique_id table with id and name descriptions
-- The id description should be uniqe and have a default value of 1
-- If table already exists, script should not fail

CREATE TABLE unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
