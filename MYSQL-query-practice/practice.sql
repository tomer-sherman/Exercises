CREATE DATABASE IF NOT EXISTS sql_practice;
USE sql_practice;

CREATE TABLE categories (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(40) NOT NULL
);

CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(40) NOT NULL,
  category_id INT NULL,
  price DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO categories (name) VALUES ('Tech'), ('Furniture'), ('Kitchen'), ('Books');

INSERT INTO products (name, category_id, price, stock) VALUES
('Laptop', 1, 4200, 5),   ('Mouse', 1, 80, 40),     ('Keyboard', 1, 250, 0),
('Monitor', 1, 900, 12),  ('Desk', 2, 1100, 3),     ('Chair', 2, 650, 0),
('Lamp', 2, 120, 25),     ('Kettle', 3, 180, 15),   ('Toaster', 3, 220, 0),
('Mug', 3, 35, 100),      ('Gift Card', NULL, 100, 50);