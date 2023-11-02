SELECT * FROM libraryschema.user;

Use libraryschema; 

CREATE TABLE User (
	id Int, 
    username CHAR(200), 
    password TEXT,
    name CHAR(200),
    address TEXT,
    phone CHAR(200),
    email CHAR(200),
	PRIMARY KEY(id)
)