# instalar postgres
# instalar pgadmin
# crear base de datos
# `CREATE DATABASE DB_PRACTICA_ORM`
# crear usuario 
`CREATE USER user_db WITH PASSWORD 'user_db';`

# dar permisos  al usuario
`GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO user_db;`
`GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO postgres;`

# crear entorno virtual o usar existente
`python3 -m venv .venv`

### abrir el entorno virtual
source .venv/bin/activate

# instalar paquetes dentro del entorno
`pip install -r requirements.txt` # esto siempre y cuando se tenga una base de paquetes preasignadas
>django, django-bootstrap-v5, crispy-forms, crispy bootstrap, psycopg2

# crear proyecto
`django-admin startproject config`
`cd config` -> para ingresar a la carperta creada

# crear aplicacion con Django
`django-admin startapp producto` -> con este comando la app se crea sola desde la terminal 

# configurar setings.py para la conexión a base de datos

# registrar aplicacion en setting.py
'producto.apps.ProductoConfig',

# realizar migraciones
`python manage.py migrate`

* Crear modelo Producto

* Registrar las url dentro de urls.py del proyecto
> config/urls.py

* Registrar paquetes django-bootstrap-v5, django-crispy-forms, crispy-bootstrap5 dentro de settings.py

* URL: crear archivo urls.py dentro del aplicativo
> producto/urls.py

* VIEWS: crear views dentro de views.py

* TEMPLATES: crear templates html dentro de la carpeta templates
> producto/templates


# -------------------x------------------

# conectar base de datos
pip install psycopg2

# usuario base de datos
usuario = postgres
clave = admin .
