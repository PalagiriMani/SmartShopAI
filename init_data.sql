DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS interactions;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT
);

CREATE TABLE interactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    action TEXT
);

INSERT INTO users (id, name) VALUES (1, 'Alice'), (2, 'Bob');
INSERT INTO products (id, name, category) VALUES
(1, 'Phone', 'Electronics'),
(2, 'Shoes', 'Fashion'),
(3, 'Laptop', 'Electronics'),
(4, 'Watch', 'Accessories');
