# --------------- Modulo 3 -------------------
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

# conectar base de datos
pip install psycopg2

# usuario base de datos
usuario = postgres
clave = admin

# --------------- Modulo 4 -------------------

# agregar campos desde la consolo o shell de django al modelo Producto 
`python manage.py shell`

```
from producto.models import Producto
Producto.objects.create(nombre='Crema', precio-5000, descripcion-'Crema de dia')
```

# listar los productos desde la consola de psql
> ingresar psql
`psql -U postgres -W -d db_practica_orm`
`SELECT * FROM producto_producto;`

# consultar los productos desde la consola de django
`python manage.py shell`
```
from producto.models import Producto
Producto.objects.all().values()
```
p1 = Producto(nombre='Crema', precio=5000, descripcion='Crema de día')
p2 = Producto(nombre='Crema', precio=5000, descripcion='Crema de día')

lista = [p1,p2]
for producto in lista:
    producto.save()


