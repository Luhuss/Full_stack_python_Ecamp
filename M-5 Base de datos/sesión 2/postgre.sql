--------------------------------------
--Variables de entorno para windows
--------------------------------------
C:\Program Files\PostgresSQL\{version}\bin
C:\Program Files\PostgresSQL\{version}\lib

C:\Program Files\PostgresSQL\15\bin
C:\Program Files\PostgresSQL\15\lin

--------------------------------------
--conectarnos a la base de datos desde psql shell
--------------------------------------
server [localhost]: localhost(127.0.0.1)
Database [postgres]: postgres
Port [5432]: 5432
Username [postgres]: postgres
Contraseña para usuario postgres: <PASSWORD> al instalar la base de datos

--------------------------------------
-- Conectarse a la base de datos desde cualquier terminal 
--------------------------------------
psql -U (username) -W -d (database_name)
psql -U postgres -W -d postgres

--------------------------------------
-- Comandos basicos de psql
--------------------------------------
help                    | ayuda general
\l                      | listar las bases de datos 
\dt                     | listar las tablas de una base de datos 
\distribución           | listar los usuarios de una base de datos
\copyright              | para ver los términos de distribución
\h                      | para ayuda de órdenes SQL 
\?                      |para ayuda órdenes psql 
\general                |o punto y coma («;») para ejecutar 
\q                      | salir de la terminal
\c {database_name}      | conectarse a una base de datos 
q                       | salir 

--------------------------------------
-- Ingresar a la base de datos: \c database_test
--------------------------------------

--- Lenguaje SQL: Lenguaje de consulta estructurada (Structured Query Language)
--- Para crear una base de dato: CREATE DATABASE {database_name};
---                            : CREATE database {database_name};
---                            : CREATE database {database_test};
-- Para eliminar una base      : DROP DATABASE {database_name};
--                             : DROP DATABASE database_test;
-- Crear 1 usuario desde el shell de PostgresSQL. :CREATE USER {username} WITH PASSWORD '{PASSWORD}'
-- Borras un usuario desde el shell de PostgresSQL: DROP USER {username};

/*
--------------------------------------------
-- Variables de entorno para windows
--------------------------------------------
C:\Program Files\PostgreSQL\{version}\bin
C:\Program Files\PostgreSQL\{version}\lib

C:\Program Files\PostgreSQL\15\bin
C:\Program Files\PostgreSQL\15\lib
--------------------------------------------
--conectar a la base de datos desde psql shell
--------------------------------------------
Server [localhost]: localhost (127.0.0.1)
Database [postgres]: postgres
Port [5432]: 5432
Username [postgres]: postgres
Contraseña para usuario postgres: <PASSWORD> al instalar la base de datos

-----------------------------------------------
-- Conectarse a la base de dato desde cualquier terminal
-----------------------------------------------
psql -U {username} -W -d {database_name}
psql -U postgres -W -d postgres

-----------------------------------------------
-- Comandos básicos de psql
-----------------------------------------------
help                         | ayuda general
\l                           | listar las bases de datos
\dt                          | listar las tablas de una base de datos      
\du                          | listar los usuarios de una base de datos
\copyright                   | para ver los términos de distribución
\h                           | para ayuda de órdenes SQL
\?                           | para ayuda de órdenes psql
\g                           |o punto y coma («;») para ejecutar la consulta
\q                           | salir del shell
\c {database_name}           | conectarse a una base de datos
q                            | salir
*/