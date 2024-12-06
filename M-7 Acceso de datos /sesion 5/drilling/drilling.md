* Muestre el modelo creado en base de datos por el modelo orm de django
`psql -U user -W -d database`
`psql -U postgres -W -d db_practica_orm`
`psql -U user_db -W -d db_practica_orm_` * archivo para el rebound sesion 3
`psql -U user_db -W -d db_practica_orm` * archivo para el rebound sesion 5
`\d producto_producto`

* Inserte registros en la base de datos mediante la terminal o consola 
    * ingresar a la terminal de python 
    `python manage.py shell`

* Crear código python para ejecutar en la terminal la creación de fabricas y productos 
'''
from producto.models import Fabrica, Producto

f1 = Fabrica.objects.create(nombre='P&G')
f2 = Fabrica.objects.create(nombre='Colgate')
f2 = Fabrica.objects.get(pk=2)
print(f2)

p1 = Producto.objects.create(nombre='Ariel Suavizante',precio=1500,
descripcion='Suavizante para la ropa', fabrica=f1)

p2 = Producto.objects.create(nombre='Crest Premium', precio=2500,
descripcion='Crema dental', fabrica=f1)

p3 = Producto.objects.create(nombre='Downy Aroma Floral', precio=3500,
descripcion='Ambientador de aroma floral', fabrica=f1)

p4 = Producto.objects.create(nombre='Protex Aloe', precio=1250,
descripcion='Jabón de baño', fabrica=f2)

p5 = Producto.objects.create(nombre='Speed Stick 24/7', precio=4500,
descripcion='Desodorante para caballeros', fabrica=f2)

p6 = Producto.objects.create(nombre='Colgate 360', precio=1850,
descripcion='Crema dental', fabrica=f2)
'''

* Mostrar en la base de datos los objetos creados
`psql -U user -W -d database`
`psql -U postgres -W -d db_practica_orm`
`psql -U user_db -W -d db_practica_orm_`
`\d producto_producto`
`SELECT * FROM producto_fabrica;`
`SELECT * FROM producto_producto;`

* para salir de la shell 
`exit()`
