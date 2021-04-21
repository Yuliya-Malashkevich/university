CREATE DATABASE university;

USE university;

CREATE TABLE student (
    id INT NOT NULL AUTO_INCREMENT,
    name_surname VARCHAR(100),
    course INT,
    physics INT,
    informatics INT,
    mathematics INT
    average_rating FLOAT,
    PRIMARY KEY (id)
    );
ALTER TABLE student ADD login VARCHAR(100);

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    login VARCHAR(100),
    password VARCHAR(100),
    status VARCHAR(100),
    PRIMARY KEY (id)
    );
