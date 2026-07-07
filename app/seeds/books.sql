DROP TABLE IF EXISTS books;

CREATE TABLE IF NOT EXISTS books (
    id serial primary key, 
    title text,
    author text
);

-- insert into books (title, author) values ('test', 'test author');
INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');
INSERT INTO books (title, author) VALUES ('The Brain', 'New Scientist');
