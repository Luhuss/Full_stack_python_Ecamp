-- Subir el ejercicio en un archivo comprimido 
-- El archivo donde se realicen las query sql con extension .txt

-- para realizar consultas
-- SELECT * FROM customer

-- Obtener el registro
-- SELECT customer_id
-- FROM customer
-- WHERE first_name = 'Naruto' AND last_name = 'Uzumaki';

-- Eliminar registro
-- DELETE FROM customer
-- WHERE customer_id = 1; 

SELECT * FROM customer ORDER BY customer_id asc 

-- Insertar un registro en Customer
INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date)
VALUES (1, 'Naruto', 'Uzumaki', 'narutouzumaki@example.com', 5, 1, CURRENT_DATE);

-- Modificar un registro en Customer
UPDATE customer
SET email = 'narutouzumaki@sakilacustomer.org', active = 0
WHERE customer_id = 600;

-- Eliminar un registro en Customer
DELETE FROM customer
WHERE customer_id = 600;

SELECT * FROM staff 

-- Insertar un registro en Staff
INSERT INTO staff (first_name, last_name, address_id, email, store_id, active, username, password, last_update, picture)
VALUES ('Sasuke', 'Uchiha', 4, 'sasuke.uchiha@example.com', 1, True, 'sasuke_u', 'password123', CURRENT_DATE, NULL);

-- Modificar un registro en Staff
UPDATE staff
SET email =  'sasukeuchiha@sakilastaff.com', active = False
WHERE staff_id = 3;

-- Eliminar un registro en Staff
DELETE FROM staff 
WHERE staff_id = 3;

-- Insertar un registro Actor
SELECT * FROM actor ORDER BY actor_id desc

INSERT INTO actor (first_name, last_name, last_update)
VALUES ('Kakashi', 'Hatake', CURRENT_DATE);

-- Modificar un registro Actor
UPDATE actor 
SET first_name = 'El ninja que copia'
WHERE actor_id = 201;

-- Eliminar un registro de Actor
DELETE FROM actor
WHERE actor_id = 201;

-- 2.- Listar todas las rental con los datos del customer dado un año y mes
SELECT rental.*, customer.first_name, customer.last_name, customer.email
FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
WHERE EXTRACT(YEAR FROM rental.rental_date) = 2005
    AND EXTRACT(MONTH FROM rental.rental_date) = 5;

-- 3.- Listar número, fecha(payment_date) y total (amount) de todas las paymet
SELECT payment_id AS Numero, payment_date AS Fecha, amount AS Total
FROM payment;

-- 4.- Listar todas las film del año 2006 que contengan un rental_rate mayor a 4.0
SELECT *
FROM film
WHERE release_year = 2006
    AND rental_rate > 4.0;

-- 5.- Realizar un Diccionario de datos que contenga:
-- Nombre de las tablas
-- Columnas
-- Si estas puedes ser nulas
-- Y su tipo de dato correspondiente

-- 1.- Tabla customer
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    store_id INT NOT NULL,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    email VARCHAR(50),  -- Puede ser nulo
    address_id INT NOT NULL,
    active BOOLEAN NOT NULL,
    create_date DATE NOT NULL
);

-- 2.- Tabla staff
CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    email VARCHAR(50),  -- Puede ser nulo
    username VARCHAR(16) NOT NULL,
    password VARCHAR(40),  -- Puede ser nulo
    store_id INT NOT NULL,
    active BOOLEAN NOT NULL
);

-- 3.- Tabla actor
CREATE TABLE actor (
    actor_id INT PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL
);

-- 4.- Tabla payment
CREATE TABLE payment (
    payment_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    staff_id INT NOT NULL,
    rental_id INT,  -- Puede ser nulo
    amount DECIMAL(5,2) NOT NULL,
    payment_date TIMESTAMP NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

-- 5.- Tabla rental
CREATE TABLE rental (
    rental_id INT PRIMARY KEY,
    rental_date TIMESTAMP NOT NULL,
    inventory_id INT NOT NULL,
    customer_id INT NOT NULL,
    return_date TIMESTAMP,  -- Puede ser nulo
    staff_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

-- 6.- Tabla film
CREATE TABLE film (
    film_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,  -- Puede ser nulo
    release_year INT,  -- Puede ser nulo
    language_id INT NOT NULL,
    rental_duration INT NOT NULL,
    rental_rate DECIMAL(4,2) NOT NULL,
    length INT,  -- Puede ser nulo
    replacement_cost DECIMAL(5,2) NOT NULL,
    rating VARCHAR(10),  -- Puede ser nulo
    last_update TIMESTAMP NOT NULL
);

-- 7.- Tabla inventory
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY,
    film_id INT NOT NULL,
    store_id INT NOT NULL,
    last_update TIMESTAMP NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film(film_id)
);

-- 8.- Tabla store
CREATE TABLE store (
    store_id INT PRIMARY KEY,
    manager_staff_id INT NOT NULL,
    address_id INT NOT NULL,
    last_update TIMESTAMP NOT NULL,
    FOREIGN KEY (manager_staff_id) REFERENCES staff(staff_id)
);





