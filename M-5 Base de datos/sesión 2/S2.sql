--PK (Primary key) - Clave Primaria
--Características de una clave primaria:
--Única: No puede haber dos registros con el mismo valor en la columna que es clave primaria.
--No nulo: Los valores de la clave primaria no pueden ser NULL.
--Identificador: Sirve para identificar de manera exclusiva a cada fila en la tabla.

--FK (Foreign KEY) - Clave Foránea
--Características de una clave foránea:
--Referencia: La clave foránea hace referencia a una clave primaria en otra tabla.
--Integridad referencial: Se asegura de que los valores que se insertan en la columna de clave foránea ya existan en la columna de clave primaria correspondiente.


--TABLA categorias // las tablas se crean en minusculas
--PK categoria_id, nombre 

--Tabala productos
--PK producto_id, nombre, precio, FK categoria_id

--TABLA categorias
--PK categoria_id, nombre

--Tabla productos
-- PK producto_id, nombre, precio, FK categoria_id

CREATE DATABASE S2;

CREATE TABLE categorias(
    categoria_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE productos(
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    precio INT,
    categoria_id INT,
    --FOREIGN KEY campo_tabla_actual REFERENCES tabla_referencia(campo_referencia)
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

INSERT INTO categorias(nombre) VALUES('ELECTRÓNICA');
INSERT INTO categorias(nombre) VALUES('ROPA');
INSERT INTO categorias(nombre) VALUES('HOGAR');

INSERT INTO productos(nombre, precio, categoria_id) VALUES
-- (nombre, precio, categoria_id)
('Teléfono', 100000, 1),
('Televisión', 150000, 1),
('Pantalon', 15000, 2),
('Polera', 20000,2),
('Tetera',50000, 3),
('Mesa', 90000, 3);

-- consultar todas las filas de la tabla categorias
SELECT * FROM categorias;

-- consultar todas las finas de la tabla productos
SELECT * FROM productos;

COMMIT; -- guardar los cambios o transacciones en la base de datos


-- eliminar tabla a traves de comandos
-- para eliminar una tabla se debe comenzar por la tabla con mas referencias o claves foraneas y luego borrar las tablas que tienen menos referencias o claves foraneas.
DROP TABLE productos;

DROP TABLE IF EXISTS productos; --Esta sentencia elimina la tabla productos solo si ya existe.
DROP TABLE IF EXISTS categorias; --Esta sentencia elimina la tabla categorias solo si ya existe.

CREATE TABLE clientes (
cliente_id SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
producto_id SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE ventas (
venta_id SERIAL PRIMARY KEY,
cliente_id INT,
producto_id INT,
fecha DATE,
FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

INSERT INTO clientes (nombre, email) VALUES
('Luis Maraboli', 'luis@example.com'),
('Ana Pérez', 'ana@example.com');

INSERT INTO productos (nombre, precio) VALUES
('Lapto', 999.99),
('Mouse', 19.99),
('Teclado', 49.99);

INSERT INTO ventas (cliente_id, producto_id, fecha) VALUES
(1, 1, '2024-09-01'),
(2, 2, '2024-09-02');
