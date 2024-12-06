###### creación de un proyecto django

1.- crear una carpeta que almacene el proyecto
    dirigirse a la carpeta y abrirla en la terminal /* paso intermedio */
2.- crear entorno local
---
python3 -m venv venv
python3 -m venv env 
python3 -m venv nombre_entorno_virtual
---
/* al crear el .venv con el punto (.) se crea como carpeta oculta, esto 
nos permite ignorar la creación del archivo .gitignore

3.- abrir el entorno virtual
source nombre_del_entorno/bin/activate
source venv/bin/activate

4.- instalar django en el entorno virtual
pip install --upgrade pip /*actualiza el pip */
pip install django /* instala django */
pip list /* para verificar los programas instalados */

5.- inicializar el proyecto django dentro de la carpeta creada en el primer paso
django-admin startproject nombre_proyecto
django-admin startproject site_django

6.- ingresar a la carpeta del proyecto creado con django-admin startproject site_django
cd nombre_proyecto
cd site_django
django-admin startapp nombre_aplicacion
django-admin startapp book /* crear una aplicacion */ 

7.- modificar el archivo settings.py para registrar el aplicativo o app creada en el punto 6, creado con django-admin startapp 
INSTALLED_APPS = [
    'book.apps.BookConfig', # agregando la app book al registro de aplicaciones instaladas
]
/* entrar a la carpeta del archivo creado cd book */

8.- ejecutar migraciones
    python manage.py migrate

9.- ejecutar el servidor local para verificar que todo este correcto
> dirigirnos a donde se encuentra el archivo manage.py dentro del proyecto
python manage.py runserver

