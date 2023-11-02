SELECT * FROM libraryschema.user;

Use libraryschema; 

drop table udjango_migrationsser;

CREATE TABLE user (
	id Int AUTO_INCREMENT, 
    username CHAR(200), 
    password CHAR(200),
    name CHAR(200),
    address TEXT,
    phone CHAR(200),
    email CHAR(200),
	PRIMARY KEY(id)
)