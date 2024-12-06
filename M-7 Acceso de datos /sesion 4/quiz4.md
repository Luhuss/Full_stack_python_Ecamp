¿Cuál es una columna de tabla que sirve a un propósito especial?

a.
Una llave primaria.

Cada tabla necesita una primary key, porque garantiza…

Pregunta 2Respuesta

a.
La accesibilidad a nivel de fila (registro).

Si no especifica primary_key = True para ningún campo en su modelo, Django…

a.
Agregará automáticamente un AutoField para contener la clave principal, por lo que no es necesario establecer primary_key = True en cualquiera de sus campos, a menos que desee anular el comportamiento predeterminado de la clave primaria.
