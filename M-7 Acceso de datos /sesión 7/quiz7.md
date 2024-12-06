Respuestas a las preguntas:
Pregunta 1: Para recuperar objetos de la base de datos, construimos un…
Respuesta correcta:
a. QuerySet, o sea una consulta a través de una clase Manager.

Un QuerySet es la forma en que Django interactúa con la base de datos para recuperar objetos. Se construye utilizando un Manager, que es una clase asociada a los modelos de Django para realizar consultas.

Pregunta 2: La afirmación “Representa una colección de objetos a partir de la base de datos, que pueden tener cero, uno o muchos filtros (filters) criterios que pueden reducir la colección basándose en parámetros dados”, corresponde a:
Respuesta correcta:
d. Un QuerySet.

Un QuerySet representa una colección de objetos obtenida de la base de datos, que se puede filtrar o modificar mediante métodos como .filter() o .exclude().

Pregunta 3: En términos de SQL, ¿a qué equivale un QuerySet?
Respuesta correcta:
d. Una declaración SELECT y un filtro es una cláusula de limitación WHERE o LIMIT.

Un QuerySet en Django es equivalente a una consulta SQL SELECT. Los filtros en el QuerySet (como .filter()) se traducen en cláusulas WHERE o LIMIT para restringir los resultados.

Pregunta 4: Podemos traer un QuerySet usando:
Respuesta correcta:
b. El Manager de su modelo.

El Manager (por defecto objects) de un modelo es la principal fuente para obtener QuerySets, permitiendo realizar consultas como Model.objects.all() o Model.objects.filter().

Pregunta 5: La definición “Es la principal fuente de QuerySets de un modelo. Actúa como una clase “raíz” de QuerySet que describe todos los objetos de la tabla de base de datos del modelo”, corresponde a:
Respuesta correcta:
d. El Manager.

El Manager es la interfaz principal para interactuar con la base de datos desde un modelo en Django. Actúa como una clase raíz para obtener QuerySets.

Resultado final:

Pregunta 1: a
Pregunta 2: d
Pregunta 3: d
Pregunta 4: b
Pregunta 5: d