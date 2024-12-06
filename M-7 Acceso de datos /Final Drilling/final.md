# paso 16
# Por medio de la consola interpretador de python (shell), realice las siguientes consultas: 
1. Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos. 
`python manage.py shell`

from laboratorio.models import Laboratorio, DirectorGeneral, Producto
laboratorio = Laboratorio.objects.all()
print('\n'.join(str(i.nombre) for i in laboratorio))

director_general = DirectorGeneral.objects.all()
print('\n'.join(str(i.nombre) for i in director_general))

producto = Producto.objects.all()
print('\n'.join(str(i.nombre) for i in producto))

# para salir de la shell
exit()

# Obtenga el laboratorio del producto cuyo nombre es 'Producto 1'
query = '''
    SELECT p.id, p.nombre AS nombre_producto, l.id, l.nombre AS nombre_laboratorio FROM laboratorio_prod p INNER JOIN laboratorio_laboratorio l ON p.laboratorio_id = l.id WHERE p.nombre = %s;
    '''

consulta1 = Producto.objects.raw(query, ['Producto 1'])
print('\n'.join(str(i.nombre_laboratorio) for i in consulta1))

consulta2 = Producto.objects.filter(nombre='Producto 1').select_related('laboratorio').values('nombre', 'laboratorio')
print('\n'.join(str(i['laboratorio']) for i in consulta2))

# Ordene todos los productos por nombre, y que muestre los valores de nombre y laboratorios
consulta4 = Producto.objects.order_by('nombre').values('nombre', 'laboratorio')
consulta5 = Producto.objects.all().order_by('nombre').values('nombre', 'laboratorio')

# Realice una consulta que imprima por pantalla lso laboratorios de todos los productos
consulta6 = Producto.objects.all().select_related('laboratorio').values('nombre', 'laboratorio')


