-- Los que salen con este simbolo #, * llevan PK id_...

-- Tabla empresa
PK rut 
nombre 
direccion 
telefono
correo 
web 

-- Tabla cliente
PK rut 
nombre 
correo 
direccion
telefono
alta

-- Tabla tipo_vehiculo
PK id_tipo_vehiculo
nombre

-- Tabla mantencion
PK id_mantencion
fecha
trabajos_realizados
FK folio

-- Tabla ventas
PK folio
fecha
monto
FK rut_cliente
FK id_vehiculo

-- Tabla vehiculo
PK id_vehiculo
patente
marca
modelo
color
precio
frecuencia_mantencion
FK id_marca
FK id_tipo_vehiculo

-- Tabla marca
PK id_marca
nombre 
