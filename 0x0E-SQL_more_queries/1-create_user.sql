-- Create user user_0d_1 with all privileges on your MySQL server and user_0d_1_pwd as passwor
-- If user already exists, the script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL
ON *.* 
TO user_0d_1@localhost;
