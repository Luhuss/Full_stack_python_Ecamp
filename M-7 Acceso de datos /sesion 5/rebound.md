> la fabrica de productos produce uno o mas productos. El producto solo puede pertences a un fabricante.

* MODEL: Construir el modelo correspondiente a la fabrica, establecer relacion una a muchos con el Producto
````
class fabrica():
    nombre = models.Charfield(max_length=100)

class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.InterField()
    descripcion = models.TextField(max_length=100)
    fabrica = models.ForeignKey(fabrica, on_delete=models.CASCADE)
```

* Realizar migraciones
`python manage.py makemigrations`
`python manage.py migrate`