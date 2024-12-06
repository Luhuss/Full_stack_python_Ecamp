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
