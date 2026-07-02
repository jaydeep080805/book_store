DROP TABLE IF EXISTS users;
-- TRUNCATE users;

CREATE TABLE IF NOT EXISTS users (
    id serial primary key,
    username text,
    password text
);

-- INSERT INTO users (username, password) VALUES ('test', 'test');