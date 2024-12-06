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

# instalar paquetes dentro del entorno - paso 3 -> este paso se hace dentro del entorno virtual
`pip install -r requirements.txt` # esto siempre y cuando se tenga una base de paquetes preasignadas
>django, django-bootstrap-v5, crispy-forms, crispy bootstrap, psycopg2

# paso 4 crear base de datos en pgadmin

# crear proyecto - paso 5
`django-admin startproject config`
`cd config` -> para ingresar a la carperta creada

# crear aplicacion con Django - paso 6
`django-admin startapp laboratorio` -> con este comando la app se crea sola desde la terminal 

# configurar setings.py para la conexión a base de datos

# registrar aplicacion en setting.py - paso 7
'laboratorio.apps.LaboratorioConfig',

* Registrar paquetes django-bootstrap-v5, django-crispy-forms, crispy-bootstrap5 dentro de settings.py
# registrar junto con el paso 7 abajo esta configuración
'bootstrap5', # registro de bootstrap5 en el proyecto
'crispy_forms', # registro de crispy forms en el proyecto # https://github.com/django-crispy-forms/crispy-bootstrap5
'crispy_bootstrap5', # registro de crispy bootstrap5 en el proyecto

# paso 8 - configurar en setings base de datos
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_practica_orm_", -> nombre base de datos
        "USER": "user_db", -> usuario
        "PASSWORD": "admin", -> clave
        "HOST": "127.0.0.1",
        "PORT": "5432",
    },
    'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }
}

# realizar migraciones - paso 9
`python manage.py makemigrations`

# realizar migraciones - paso 10
`python manage.py migrate`

# conectar base de datos - paso 11
pip install psycopg2

# paso 12 crear superUsuario
python manage.py createsuperuser

# paso 13 * Registrar las url dentro de urls.py del proyecto
> config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laboratorio/', include('laboratorio.urls')),
    path('', include('laboratorio.urls'))
]

# paso 14 * URL: crear archivo urls.py dentro del aplicativo 
> producto/urls.py

from django.urls import path, include

urlpatterns = [
    
]

# paso 15 -> esto puede variar dependiendo la solicitud
* Crear modelo Producto

from django.db import models
from django.core.validators import MinValueValidator

from datetime import date 

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/5.1/ref/validators/#minvaluevalidator
    fecha_fabricacion = models.DateTimeField(validators=[MinValueValidator(limit_value=date(2015, 1, 1))])
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


# luego de esto realizar migraciones nuevamente
`python manage.py makemigrations`
`python manage.py migrate`

# paso 16 configurar admin

from django.contrib import admin

from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    list_filter = ('nombre')

class DirectorioGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    list_filter = ('nombre')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_fabricacion' 'precio_costo', 'precio_venta')
    list_display_links = ['nombre']
    list_filter = ('nombre')    

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorioGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)


* VIEWS: crear views dentro de views.py

* TEMPLATES: crear templates html dentro de la carpeta templates
> producto/templates


# -------------------x------------------



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
