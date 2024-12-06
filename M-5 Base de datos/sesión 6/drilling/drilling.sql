-- 1. Listar todos los vehiculos que no han sido vendidos
SELECT v.* FROM vehiculo v
LEFT JOIN venta ven
ON v.id_vehiculo = ven.id_vehiculo
WHERE ven.id_vehiculo IS NULL;

SELECT * FROM vehiculo
LEFT JOIN venta
ON vehiculo.id_vehiculo = venta.id_vehiculo
WHERE venta.id_vehiculo IS NULL;

-- 2. Listar todas las ventas de enero del 2020 con las columnas : folio, fecha, monto, nombre y rut del cliente, patente y modelo del vehiculo, nombre de la marca.
-- tabla venta ven = ven.folio, ven.fecha, ven.monto
-- tabla cliente c = c.nombre, c.rut
-- tabla vehiculo v = v.patente, v.modelo
-- tabla marca m = m.nombre
SELECT ven.folio, ven.fecha, ven.monto, c.nombre, c.rut, v.patente, v.modelo, m.nombre FROM venta ven
JOIN cliente c ON ven.rut_cliente = c.rut
JOIN vehiculo v ON ven.id_vehiculo = v.id_vehiculo
JOIN marca m ON v.id_marca = m.id_marca
WHERE EXTRACT(MONTH FROM ven.fecha) = 1 
AND EXTRACT(YEAR FROM ven.fecha) = 2020;

--3. Sumar las ventas por mes y marca del año 2020
-- tabla venta ven = ven.monto, ven.fecha
-- tabla vehiculo v
-- tabla marca m = m.nombre
SELECT m.nombre AS marca, SUM(ven.monto) AS total_ventas
FROM venta ven
JOIN vehiculo v ON ven.id_vehiculo = v.id_vehiculo
JOIN marca m ON v.id_marca = m.id_marca
WHERE EXTRACT(YEAR FROM ven.fecha) = 2020
GROUP BY m.nombre;

--4. Listar rut y nombre de las tablas cliente y empresa
SELECT rut, nombre FROM cliente
UNION
SELECT rut, nombre FROM empresa;

SELECT c.rut AS rut_cliente, c.nombre AS nombre_cliente, e.rut AS rut_empresa, e.nombre AS nombre_empresa 
FROM cliente c
CROSS JOIN empresa e;