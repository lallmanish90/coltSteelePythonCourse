-- 
-- creating a table

-- - to create a new file ,  .open filename.txt / will open the file if it exists or create one 
-- -data is stored locally on that session on terminal
-- -if you want to save the data , have to open the file first in the termal inside sqlite3 

-- 

-- CREATE TABLE dogs (
--     name TEXT,
--     breed TEXT,
--     age INTEGER
-- );

INSERT INTO dogs (name,age,breed) VALUES ("Champ", 4, "Husky");
INSERT INTO dogs (name,age,breed) VALUES ("Rose", 11, "Chihuahua");
INSERT INTO dogs (name,age,breed) VALUES ("Moose", 5, "lab");
INSERT INTO dogs (name,age,breed) VALUES ("Piggy", 9, "Corgi");