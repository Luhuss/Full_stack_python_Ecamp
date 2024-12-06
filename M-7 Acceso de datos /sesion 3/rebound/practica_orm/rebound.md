# instalar postgres
# instalar pgadmin
# crear base de datos
# `CREATE DATABASE DB_PRACTICA_ORM`
# crear usuario 
`CREATE USER user_db WITH PASSWORD 'user_db';`

# dar permisos  al usuario
`GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO user_db;`
`GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO postgres;`

# crear entorno virtual o usar existente - paso 1
`python3 -m venv .venv`

### abrir el entorno virtual - paso 2
source .venv/bin/activate

# instalar paquetes dentro del entorno - paso 3
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





from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def listar(request):
    productos = Producto.objects.all()
    return render(request, 'listar_producto.html', {'productos':productos})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_producto'))
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html', {'producto_form':form}) 
    
def editar(request, producto_id):
    producto = get_object_or_404(request, producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Datos inválidos para editar el producto')
            return HttpResponseRedirect(reverse('editar_producto', args=[producto.id]))
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'producto_form':form, 'producto_id': producto_id})    
    
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(request, producto_id)
    producto.delete()
    messages.info(request, 'Producto eliminado')
    return redirect('listar_producto')    


