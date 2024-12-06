# crear el modelo Producto
>producto/models.py

# Generar migraciones
`python manage.py makemigrations`
`python manage.py migrate`

# Mostrar sql mediante el manage.py
`python manage.py sqlmigrate producto 0001`

# Ingresar al shell de postgres y consultar la base de datos, revisando si se creó la tabla producto
psql -U username -W -d database_name
psql -U user_db -W -d db_practica_orm_
Password:
\d
\d producto_producto

# Mostrar todas las bases de datos:
\l

# Conectarse a otra base de datos:
\c nombre_de_la_base_de_datos

# Listar todas las tablas en la base de datos actual:
\dt

# Ver la estructura de una tabla específica:
\d nombre_de_la_tabla

# Ejecutar una consulta SQL (asegúrate de terminar con un punto y coma):
SELECT * FROM nombre_de_la_tabla;

# Salir de psql:
\q

# Obtener ayuda sobre comandos de SQL:
\h nombre_comando_sql

Ejemplo:

sql
Copiar código
\h SELECT
Obtener ayuda sobre los comandos de psql:

sql
Copiar código
\?