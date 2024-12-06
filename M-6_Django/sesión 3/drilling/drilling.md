#### crear carpeta para almacenar el proyecto
mkdir practica

### ingresar a la carpeta creada
cd proyecto

### crear entorno virtual django_development
python3 -m venv django_development
python3 -m venv django_development1

### abrir el entorno virtual
source jango_development/bin/activate
source jango_development1/bin/activate

### instalar django en el entorno virtual
pip install --upgrade pip /*actualiza el pip */
pip install django /* instala django */
pip list /* para verificar los programas instalados */

### eliminar entorno
rm -rf ./django_development1

### instalar pip
pip install --upgrade pip

### instalar django 4.0.5
pip install django==4.0.5

### crear un proyecto django
django-admin startproject nombre_proyecto
django-admin startproject project

### ubicarse en la carpeta creada
cd project

### crear la app
django-admin startapp app

### modificar el archivo settings.py para registrar el aplicativo o app creada en el punto 6, creado con django-admin startapp 
INSTALLED_APPS = [
    'app.apps.AppConfig'
]

### ejecutar migraciones
    python manage.py migrate

### ejecutar el servidor local para verificar que todo este correcto
python manage.py runserver
