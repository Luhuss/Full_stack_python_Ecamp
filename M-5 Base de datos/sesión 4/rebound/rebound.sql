-- 1.- Crear una base de datos llamada empresa
CREATE DATABASE empresa;

-- Usar la base de datos creada
USE empresa;
USE DATABASE empresa;

-- 2.- Crear una tabla llamada departamentos
CREATE TABLE departamentos(
    id_departamento SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(100)
);

-- 3.- Crear tabla llamada empleados
CREATE TABLE empleados(
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(100),
    salario DECIMAL(10,2),
    fecha_contratacion DATE,
    id_departamento INT 
);

CREATE TABLE empleados(
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(100),
    salario DECIMAL(10,2),
    fecha_contratacion DATE,
    id_departamento INT,
    CONSTRAINT fk_empleados_id_departamento FOREIGN KEY (id_departamento) REFERENCES departamentos (id_departamento)
);

ALTER TABLE empleados ADD CONSTRAINT fk_empleados_id_departamento FOREIGN KEY (id_departamento) REFERENCES departamentos (id_departamento);

-- 4.- Modificar tabla empleados, añadiendo una columna llamada email (cadena de caracteres, 100 caractereses)
ALTER TABLE empleados ADD COLUMN email VARCHAR(100);

-- Borra columna email
ALTER TABLE {tabla} DROP COLUMN {nombre_columna};
ALTER TABLE empleados DROP COLUMN email;

-- 5.- Cambiar el nombre de la tabla empleados a trabajadores
ALTER TABLE empleados RENAME TO trabajadores;

-- 6.- Borra la tabla de departamentos
DROP TABLE trabajadores;
DROP TABLE departamentos;

