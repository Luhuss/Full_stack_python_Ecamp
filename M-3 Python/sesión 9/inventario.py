'''
Sistema de Gestión de Inventario
Enunciado: Crea un programa que gestione el inventario de una tienda. El programa debe permitir al usuario agregar, eliminar y actualizar productos en el inventario. Cada producto debe tener un nombre, una cantidad y un precio. Además, el programa debe permitir al usuario ver el inventario completo y calcular el valor total del inventario.
Utilizar un diccionario para representar el inventario 
{“nombre”: {“cantidad”: “5”, “precio”:”5000”}}
'''

# Diccionario para representar el inventario
inventario = {}

def agregar_producto(nombre, cantidad, precio):
    if nombre in inventario:
        print(f'El producto {nombre} ya existe en el inventario.')
    else:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print(f'Producto {nombre} agregado correctamente.')

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f'Producto {nombre} eliminado correctamente.')
    else:
        print(f'El producto {nombre} no existe en el inventario.')

def actualizar_producto(nombre, cantidad=None, precio=None):
    if nombre in inventario:
        if cantidad is not None:
            inventario[nombre]['cantidad'] = cantidad
        if precio is not None:
            inventario[nombre]['precio'] = precio
        print(f'Producto {nombre} actualizado correctamente.')
    else:
        print(f'El producto {nombre} no existe en el inventario.')

def mostrar_inventario():
    if not inventario:
        print('El inventario está vacío.')
    else:
        print('Inventario:')
        for nombre, detalles in inventario.items():
            print(f"{nombre} - Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']}")

def calcular_valor_total():
    valor_total = 0
    for detalles in inventario.values():
        valor_total += detalles['cantidad'] * detalles['precio']
    print(f'Valor total del inventario: ${valor_total}')

# Ejemplo de uso
while True:
    opcion = input('''Seleccione una opción:
    1) Agregar producto
    2) Eliminar producto
    3) Actualizar producto
    4) Ver inventario
    5) Calcular valor total del inventario
    6) Salir
    Opción: ''').strip()

    if opcion == '1':
        nombre = input('Ingrese el nombre del producto: ').strip()
        cantidad = int(input('Ingrese la cantidad: '))
        precio = float(input('Ingrese el precio: '))
        agregar_producto(nombre, cantidad, precio)

    elif opcion == '2':
        nombre = input('Ingrese el nombre del producto a eliminar: ').strip()
        eliminar_producto(nombre)

    elif opcion == '3':
        nombre = input('Ingrese el nombre del producto a actualizar: ').strip()
        cantidad = input('Ingrese la nueva cantidad (o presione Enter para no cambiarla): ').strip()
        precio = input('Ingrese el nuevo precio (o presione Enter para no cambiarlo): ').strip()

        cantidad = int(cantidad) if cantidad else None
        precio = float(precio) if precio else None
        actualizar_producto(nombre, cantidad, precio)

    elif opcion == '4':
        mostrar_inventario()

    elif opcion == '5':
        calcular_valor_total()

    elif opcion == '6':
        print('Saliendo del sistema de gestión de inventario...')
        break

    else:
        print('Opción inválida. Intente de nuevo.')

'''
Descripción del programa:
Agregar Producto: Permite al usuario agregar un nuevo producto al inventario.
Eliminar Producto: Elimina un producto existente en el inventario.
Actualizar Producto: Permite modificar la cantidad y/o el precio de un producto existente.
Ver Inventario: Muestra todos los productos en el inventario junto con sus cantidades y precios.
Calcular Valor Total: Calcula el valor total del inventario basado en las cantidades y precios de los productos.
Salir: Termina el programa.

'''