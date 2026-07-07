DROP TABLE IF EXISTS movies;

CREATE TABLE IF NOT EXISTS movies (
    id serial primary key, 
    title text,
    release_year int
);

INSERT INTO movies (title, release_year) VALUES ('Interstellar', 2009);
INSERT INTO movies (title, release_year) VALUES ('Inception', 2009);