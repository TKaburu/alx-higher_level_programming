-- Create hbtn_0d_2 database and user_0d_2 user with the password as user_0d_2_pwd
-- user_0d_2 should have SELECT privilage in hbtn_0d_2
-- If database and username already exists, it should not throw an error

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
