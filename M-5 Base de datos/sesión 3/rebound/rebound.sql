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
    celular VARCHAR(15),
    alta BOOLEAN
);

-- Venta
CREATE TABLE venta(
    folio SERIAL PRIMARY KEY,
    fecha DATE,
    monto INT,
    id_vehiculo INT,
    rut_cliente VARCHAR(10)
);

-- Mantención 
CREATE TABLE mantencion(
    id_mantencion SERIAL PRIMARY KEY,
    fecha DATE,
    trabajos_realizados VARCHAR(1000),
    folio INT
);

-- Tipo de vehiculo
CREATE TABLE tipo_vehiculo(
    id_tipo_vehiculo INT PRIMARY KEY,
    nombre VARCHAR(120)
);

-- Vehiculo
CREATE TABLE vehiculo(
    id_vehiculo SERIAL PRIMARY KEY,
    patente VARCHAR(10),
    marca VARCHAR(20),
    modelo VARCHAR(20),
    color VARCHAR(15),
    precio INT,
    frecuencia_mantencion INT,
    id_marca INT,
    id_tipo_vehiculo INT
);

-- Tabla marca
CREATE TABLE marca(
    id_marca SERIAL PRIMARY KEY,
    nombre VARCHAR(120)
);

ALTER TABLE mantencion ADD CONSTRAINT fk_mantencion_folio FOREIGN KEY (folio) REFERENCES venta(folio);

ALTER TABLE venta ADD CONSTRAINT fk_venta_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES cliente(rut);
ALTER TABLE venta ADD CONSTRAINT fk_venta_id_vehiculo FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id_vehiculo);

ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_marca FOREIGN KEY (id_marca) REFERENCES marca(id_marca);
ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_tipo_vehiculo FOREIGN KEY (id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo);