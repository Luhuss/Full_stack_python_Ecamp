-- 1.- crear base de datos peliculas
CREATE TABLE peliculas(
    id INT PRIMARY KEY,    -- 'id' es la clave primaria, identifica de manera única a cada película
    pelicula VARCHAR(255), -- 'pelicula' es el nombre de la película (hasta 255 caracteres)
    estreno INT,           -- 'estreno' es el año de estreno de la película
    director VARCHAR(255)  -- 'director' es el nombre del director de la película (hasta 255 caracteres)
);

-- 2.- crear tablas basadas en archivos.csv
CREATE TABLE reparto(
    id_pelicula INT,   -- 'id_pelicula' es una referencia a la película, clave foránea que conecta con 'pelicula'
    actor VARCHAR(255) -- 'actor' es el nombre del actor (hasta 255 caracteres)
    CONSTRAINT fk_reparto_id_peliculas FOREIGN KEY (id_pelicula) REFERENCES peliculas(id) -- Definición de la clave foránea
);
COMMIT; -- Confirma los cambio (creacion de las tablas)

-- 3.- cargar datos a las tablas, poblar tabla peliculas y reparto
\COPY "peliculas" FROM /Users/luismaraboli/Documents/E-CAMP/Curso Python/Full Stack Python/M-5 Base de datos/sesión 5/drilling/peliculas.csv WITH CSV; 
\COPY "reparto" FROM /Users/luismaraboli/Documents/E-CAMP/Curso Python/Full Stack Python/M-5 Base de datos/sesión 5/drilling/reparto.csv WITH CSV;
-- Carga datos en la tabla 'reparto' y 'peliculas' desde un archivo CSV especificado
-- al cargar los datos se debe agregar la ruta desde donde se esta tomando el archivo.

-- 4.- Consultas para verificar el contenido de las tablas
SELECT * FROM peliculas; -- Selecciona y muestra todas las filas de la tabla 'peliculas' 
SELECT * FROM reparto;   -- Selecciona y muestra todas las filas de la tabla 'reparto' 

-- 5.- Eliminar las tablas y datos
DROP TABLE reparto;         -- Elimina la tabla 'reparto' completamente
DROP TABLE peliculas;       -- Elimina la tabla 'peliculas' completamente
TRUNCATE TABLE peliculas;   -- Vaciar la tabla 'peliculas' si no se desea eliminar completamente la estructura

-- 7.- Listar todos los actores que aparecen en la pelicula Titanic, Indicando... pelicula, estreno, director, reparto
SELECT p.pelicula, p.estreno, p.director, p.actor 
FROM peliculas AS p 
JOIN reparto as r
ON p.id = r.id_pelicula
WHERE pelicula = 'Titanic'; -- Buscar todas las películas que tienen el título 'Titanic' y mostrar actores, director y año de estreno

-- 8. Listar los 10 directores más populares, indicando nombre del director y la cantidad de películas que dió.
SELECT director, COUNT(*) AS cantidad_peliculas
FROM peliculas
GROUP BY director                   -- Agrupar por el nombre del director
ORDER BY cantidad_peliculas DESC    -- Ordenar de mayor a menor por el número de peliculas
LIMIT 10;                           -- Mostrar solo los 10 primeros resultados

-- 9. Indicar cuantos actores distintos hay
SELECT COUNT(DISTINCT actor) AS total_distintos FROM reparto;
-- Mostrar solo los actores distintos y contar cuántos hay en total
SELECT DISTINCT actor FROM reparto; -- Selecciona y muestra todos los actores únicos en la tabla 'reparto'

-- 10. Indicar las peliculas estrenadas entre los años 1990 y 1999. Ordenar por año ascendente
SELECT pelicula, estreno FROM peliculas 
WHERE estreno 
BETWEEN 1990 AND 1999
ORDER BY pelicula ASC;      -- Ordena por el nombre de la pelicula (orden ascendente)

SELECT pelicula, estreno FROM peliculas 
WHERE estreno 
BETWEEN 1990 AND 1999
ORDER BY estreno ASC;  -- Ordena por el nombre de la pelicula (orden ascendente)

-- 11. Listar los actores de la pelicula mas nueva
SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
ORDER BY p.estreno DESC; -- Ordena por el año de estreno de manera descendente (la más reciente primero)

-- Obtener el año de estreno más reciente
SELECT MAX(estreno) FROM peliculas;

-- Mostrar los actores de la pelicula con el año de estreno más reciente
SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE estreno = (SELECT MAX(estreno) FROM peliculas);

SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE p.estreno = (SELECT MAX(estreno) FROM peliculas);

-- Otra consulta similar para la película estrenada en 2008
SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE p.estreno = 2008;

-- 12.- Inserte los datos de una nueva pelicula solo en memoria y otra pelicula en el disco duro 
BEGIN;
SAVE POINT uno;         -- Crear un punto de guardado
INSERT INTO peliculas VALUES(101, 'Harry Potter', 2003, 'Chris Columbus'); -- Inserta una película en memoria

SAVE POINT dos;         -- Crea un segundo punto de guardado
INSERT INTO peliculas VALUES(102, 'Joker', 2024, 'Director'); -- Inserta otra película en memoria

ROLLBACK TO dos;        -- Revertir los cambios hasta el segundo punto (eliminar la inserción de 'Joker')
COMMIT;                 -- Confirmar la inserción de 'Harry Potter'

-- 13.- Actualice 5 directores utilizando rollback para deshacer el registro
UPDATE peliculas SET autor = 'Miguel de Cervantes' WHERE id = 1;        -- Cambiar el director en el registro con id 1
UPDATE peliculas SET autor = 'Antoine SaintExupery' WHERE id = 2;       -- Cambiar el director en el registro con id 2
UPDATE peliculas SET autor = 'Maquiavelo' WHERE id = 3;                 -- Cambiar el director en el registro con id 3
UPDATE peliculas SET autor = 'Henry Kissinger' WHERE id = 4;            -- Cambiar el director en el registro con id 4
UPDATE peliculas SET autor = 'Miguel de Cervantes' WHERE id = 5;        -- Cambiar el director en el registro con id 5

UPDATE peliculas SET director = Case
    WHEN id = 1 THEN 'Miguel de Cervantes'
    WHEN id = 2 THEN 'Antoine SaintExupery'
    WHEN id = 3 THEN 'Maquiavelo'
    WHEN id = 4 THEN 'Henry Kissinger'
    WHEN id = 5 THEN 'Miguel de Cervantes'
    END 
WHERE id IN (1, 2, 3, 4, 5);

ROLLBACK        -- Revertir todas las actualizaciones hechas en esta sesión

-- 14.- Inserte 3 actores a la pelicula Rambo utilizando SAVEPOINT
SELECT * FROM peliculas WHERE LOWER(pelicula) LIKE '%rambo%';       -- Buscar películas cuyo nombre contenga "rambo"

BEGIN;
SAVEPOINT uno;    -- Crea un punto de guardado
INSERT INTO reparto VALUES
(72, 'Fulanito'),  -- Inserta tres actores en la pelicula con id 72
(72, 'Mengano'),
(73, 'Sutano');
ROLLBACK TO uno;  -- Revertir todos los cambios hasta el punto de guardado 'uno'

-- 15.- Elimina las peliculas estrenadas el año 2008 solo en memoria
BEGIN;
ALTER TABLE reparto DROP CONSTRAINT fk_reparto_id_peliculas; -- Eliminar la restricción de clave foránea para poder borrar registros
SELECT * FROM peliculas WHERE estreno = 2008;
DELETE FROM peliculas WHERE estreno = 2008; -- Borra peliculas con año de estreno 2008
ROLLBACK; -- Revertir la operación de borrado


BEGIN;
ALTER TABLE reparto DISABLE TRIGGER ALL;    -- Desactivar todos los disparadores (triggers) antes de eliminar
ALTER TABLE peliculas DISABLE TRIGGER ALL;
DELETE FROM peliculas WHERE estreno = 2008; -- Borrar nuevamente las películas estrenadas en 2008

ALTER TABLE reparto ENABLE TRIGGER ALL;     -- Volver a activar los disparadores
ALTER TABLE peliculas ENABLE TRIGGER ALL;
ROLLBACK;       -- Revertir todos los cambios

-- 16.- Inserte 2 actores para cada pelicula estrenada el 2001
SELECT * FROM peliculas WHERE estreno = 2008;
-- 13 "El Señor de los anillos: La comunidad del anillo" 2001 "Peter Jackson"
-- 16 "Monstruos S.A." 2001 "Pete Docter"
-- 55 "El viaje de Chihiro" 2001 "Hayao Miyazaki"
-- 78 "Amada" 2001 "Jean-Pierre Jeunet"
-- 94 "Ocean´s Eleven" 2001 "Steven Spielberg"
-- 99 "Mouling Rouge" 2001 "Baz Luhrmann"

BEGIN
SAVEPOINT uno; -- Crea un punto de guardado 
INSERT INTO reparto VALUES
(13, 'Fulanito'),       -- Inserta actores para la pelicula con id 13
(13, 'Perez'),
(16, 'Mengano'),
(16, 'Maria'),
(55, 'Sutano'),
(55, 'Jose'),
(78, 'Karla'),
(78, 'Javiera'),
(94 'Jacinto'),
(94, 'Luis'),
(99, 'Beatriz'),
(99, 'Natalia');
ROLLBACK TO uno; -- Revertir los cambios hasta el punto de guardado 'uno'


