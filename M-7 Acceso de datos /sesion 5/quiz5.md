Respuestas a las preguntas:
Pregunta 1: ¿Para qué se utiliza el campo ForeignKey?
Respuesta correcta:
a. Establecer una relación de 1 registro a varios registros.

El campo ForeignKey se utiliza para establecer una relación muchos a uno (o uno a varios) entre dos modelos. Por ejemplo, un modelo Author puede estar relacionado con muchos registros del modelo Book, pero cada libro pertenece a un solo autor.

Pregunta 2: ¿Para qué se utiliza el campo ManyToManyField?
Respuesta correcta:
b. Relacionar varios registros entre sí, creando una nueva tabla que contiene los IDs de los modelos.

El campo ManyToManyField crea una relación muchos a muchos entre dos modelos, donde varios registros de un modelo pueden estar relacionados con varios registros de otro modelo. Django utiliza una tabla intermedia para almacenar los IDs de ambas tablas.

Pregunta 3: ¿Qué es una relación muchos a uno?
Respuesta correcta:
a. Significa que un registro de la tabla A puede tener muchos registros coincidentes en la tabla B, pero un registro de la tabla B sólo tiene un registro coincidente en la tabla A.

Un ejemplo clásico de esta relación es un modelo Departamento y un modelo Empleado: un departamento puede tener muchos empleados, pero cada empleado pertenece a un único departamento.

Pregunta 4: ¿Cuándo se utiliza una relación muchos a uno?
Respuesta correcta:
a. Se utiliza con frecuencia para describir clasificaciones o agrupaciones.

La relación muchos a uno se usa comúnmente para modelar jerarquías o agrupaciones, como un conjunto de registros que pertenecen a una categoría o clase.

Pregunta 5: La afirmación "Se aplica cuando creamos una clave foránea utilizando esta opción, se elimina las filas de referencia en la tabla secundaria cuando la fila referenciada se elimina en la tabla primaria que tiene una clave primaria", corresponde a:
Respuesta correcta:
c. Borrado en cascada.

El borrado en cascada (on_delete=models.CASCADE) asegura que cuando se elimina un registro de la tabla principal, todos los registros relacionados en la tabla secundaria también se eliminan automáticamente.

