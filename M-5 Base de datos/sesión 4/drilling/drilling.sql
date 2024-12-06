-- Empresa
CREATE TABLE empresa(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120),
    direccion VARCHAR(120),
    telefono VARCHAR(15),
    correo VARCHAR(80),
    web VARCHAR(50)
);

-- Cliente
CREATE TABLE cliente(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120),
    correo VARCHAR(80),
    direccion VARCHAR(120),
    celular VARCHAR(15)
);

-- Herramienta
CREATE TABLE herramienta(
    id_herramienta INT PRIMARY KEY,
    nombre VARCHAR(120),
    precio_dia INT
);

-- Arriendo 
CREATE TABLE arriendo(
    folio INT PRIMARY KEY,
    fecha DATE,
    dias INT,
    valor_dia INT,
    garantia VARCHAR(30),
    id_herramienta INT,
    rut_cliente VARCHAR(10)
);

-- 1.- Inserte los datos de una empresa
INSERT into empresa VALUES('11111111-1','Arrienda Herramientas','0123 Avenida Real',1234567890,'datosarriendo@herramientas.es','arrimientas.es');


-- 2.- Inserte 5 herramientas
INSERT into herramienta VALUES
(1,'Taladro Electrico',10000),
(2,'Cierra Electrica',20000),
(3,'Pistola de Clavos',30000),
(4,'Lijadora',40000),
(5,'Serrucho Electrico',50000);

-- 3.- Inserte 3 clientes
INSERT into cliente VALUES
('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);							

-- 4.- Elimina el ultimo cliente
--DELETE FROM {tabla} WHERE {atributo_campo} = {valor};
DELETE FROM cliente WHERE rut = '44444444-4';

-- 5.- Elimina la primera herramienta
--DELETE FROM {tabla} WHERE {atributo_campo} = {valor};
DELETE FROM herramienta WHERE id_herramienta = 1;

-- 6.- Inserta 2 arriendos para cada clientes
INSERT into arriendo (folio, fecha, dias, valor_dia, garantia, id_herramienta, rut_cliente)
VALUES
(1,'12/11/22',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
(2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
(3,'12/11/22',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
(4,'12/11/22',3,40000,'Eficacia en solo 3 dias',4,'33333333-3');

-- 7.- Modifique el correo del primer cliente
UPDATE cliente SET correo = 'j.perez@mail.com' WHERE rut = '22222222-2';

-- 8.- Liste todas las herramientas
SELECT * FROM herramienta;

-- 9.- Liste todos los arriendos del cliente '33333333-3'
SELECT * FROM arriendo WHERE rut_cliente = '33333333-3';

-- 10.- Liste los clientes cuyo nombre contenga una 'a'
SELECT * FROM cliente WHERE nombre LIKE '%a%'; 
SELECT * FROM cliente WHERE UPPER(nombre) LIKE '%A%'; 
SELECT * FROM cliente WHERE LOWER(nombre) LIKE '%a%'; 

-- 11.- Obtenga el nombre de la segunda herramienta insertada.
SELECT * FROM herramienta WHERE id_herramienta = 2;

-- 12.- Modifique los primeros 2 arriendos insertados con fecha 15-01-2020
SELECT * FROM arriendo;
UPDATE arriendo SET fecha = '2020/01/15' WHERE folio = 1;
UPDATE arriendo SET fecha = '2020/01/15' WHERE folio = 2;

-- 13.- Liste folio, fecha y valorDia de los arriendos enero del 2022
SELECT folio, fecha, valor_dia FROM arriendo
WHERE
EXTRACT(MONTH FROM fecha) = 01 AND EXTRACT(YEAR FROM fecha) = 2022;

-- 14.- Recuperar clientes que empiencen con Ma
SELECT * FROM cliente;
SELECT * FROM cliente WHERE (nombre) LIKE 'Ju%';

-- 15.- Recuperar herramientas que tienen un precio diario de 20000.
SELECT * FROM herramienta;
SELECT * FROM herramienta WHERE precio_dia >= 20000;

-- 16.- Contar el número de arriendos que ha hecho cada cliente.
SELECT * FROM arriendo;
SELECT rut_cliente, COUNT(*) as total_arriendos
FROM arriendo
GROUP BY rut_cliente

-- 17.- Calcular el valor total de arriendos para cada cliente.
SELECT * FROM arriendo;
SELECT rut_cliente, SUM(dias * valor_dia) AS valor_total
FROM arriendo
GROUP BY rut_cliente;
HAVING COUNT(*) > 1;

-- 18.- Recuperar clientes que han hecho más de 1 arriendos.

-- 19.- Recuperar todos los clientes y ordenarlos por su nombre.


