-- Create hbtn_0d_usa database and cities table within database with id, name and state_id descriptions
-- id is  unique, auto generated, can’t be null and is a primary key
-- name can't be NULL
-- state_id can’t be null and must be a FOREIGN KEY that references to id of the states table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
