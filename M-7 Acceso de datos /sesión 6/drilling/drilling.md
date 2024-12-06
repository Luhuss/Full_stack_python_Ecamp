1. Agregue los siguientes campos a los modelos, y genere las migraciones correspondientes.
Fábrica: pais = Tipo cadena de 100 caracteres.
Producto: fecha_vencimiento = Tipo fecha, que puede ser nulo o vacío.
```
class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=100, blank=True, null=True) 

class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
```
* Realizar migraciones
`python manage.py makemigrations`
`python manage.py sqlmigrate producto 0003` -> este codigo funciono 

`python manage.py sqlmigrate producto 0003`
`python manage.py migrate producto 0003`

2. Revierta la migración actual a la 0001_inicial.py, y genere una nueva migración llamada: agregacion_de_relacion_y_campos
`python manage.py migrate producto 0002`
`python manage.py showmigrations`
`python manage.py migrate producto 0001`
`python manage.py migrate producto --name agregacion_de_relacion_y_campos` | nombrar una migracion
`python manage.py makemigrations producto --name agregacion_de_relacion_y_campos` -> este codigo funciono 

`python manage.py migrate`