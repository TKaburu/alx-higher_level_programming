-- Convert Database to UTF8

ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8 COLLATE utf8_general_ci;
USE hbtn_0c_0;
ALTER TABLE first_table
CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256)
CHARACTER SET utf8 COLLATE utf8_general_ci;
