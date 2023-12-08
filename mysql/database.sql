CREATE DATABASE infodb;
USE infodb;

CREATE TABLE users (
    id int not null AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
    PRIMARY KEY (id)
);

INSERT INTO users(name, email)
VALUES("John", "jhon@gmail.com"), ("Emma", "emma@gmail.com"); 