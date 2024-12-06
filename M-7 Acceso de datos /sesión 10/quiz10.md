Respuestas
Pregunta 1: ¿Cuál se utiliza para especificar qué modelos deben operar en qué bases de datos para cada clase de operación de base de datos?
Respuesta:
b. dbrouters.py
El archivo dbrouters.py se utiliza en Django para definir reglas que determinan qué base de datos se usa para qué modelo y operación. Esto es útil en configuraciones con múltiples bases de datos.

Pregunta 2: ¿Qué especifica la variable ROOT_URLCONF en el archivo settings.py?
Respuesta:
b. El nombre del archivo de enrutamiento global.
La variable ROOT_URLCONF en settings.py define el módulo Python que contiene la configuración global de rutas de la aplicación. Generalmente, apunta al archivo urls.py principal de tu proyecto.

Pregunta 3: En el archivo urls.py, use:
Respuesta:
d. La variable urlpatterns para indicar el enrutamiento.
En Django, urlpatterns es una lista que contiene las rutas definidas para la aplicación. Estas rutas mapean URLs a vistas específicas o a otros enrutadores.

Explicación adicional:
dbrouters.py:

Permite definir reglas personalizadas para asignar operaciones de modelos a bases de datos específicas.
Se configura en la variable DATABASE_ROUTERS en settings.py.
ROOT_URLCONF:

Especifica el archivo principal para la configuración de URLs.
Por defecto, apunta a urls.py dentro del proyecto.
urlpatterns:

Es la lista principal en urls.py donde se definen rutas utilizando funciones como path() o re_path().
Ejemplo:
python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]