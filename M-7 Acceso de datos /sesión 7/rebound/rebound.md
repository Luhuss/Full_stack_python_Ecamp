1. Partiendo del modelo creado anteriormente (Fabrica y Productos), procedemos a agregar el
modelo al administrador de Django para incluir los registros, tanto para Fábricas como para
Productos.

* crear clases que representen a los modelos dentro del admin.py
```
from django.contrib import admin
from .models import Fabrica, Producto

# Register your models here.
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    list_display_links = ['nombre', 'pais']
    list_filter = ('nombre', 'pais')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_vencimiento', 'precio', 'fabrica')
    list_display_links = ['id', 'nombre']
    list_filter = ('nombre', 'fabrica')

# el registro siempre debe ir al final del código
admin.site.register(Fabrica, FabricaAdmin) 
admin.site.register(Producto, ProductoAdmin)
```

* crear superuser mediante manage.py , ubicarse en la terminal a la altura del archivo manage.py
`python manage.py createsuperuser`
* usuario: admin
* clave: admin
* mail: admin@gmail.com
