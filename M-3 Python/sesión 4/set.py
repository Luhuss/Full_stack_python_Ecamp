# set
# set de datos o conjuntos de datos, es una estructura de datos que no permite duplicados
# se pueden realizar operaciones de conjuntos como union, intersección, diferencia, etx.
# se utilizan {} para declarar un set de datos

# declarar variables
# snake_case = variable_uno
# camelCase = variableUno
variable_uno = 8 # int (entero)
variable_dos = 10.5 # float (flotante o decimal)
variable_tres = 'ejercicio' # str (string)

# crear set de datos
set_datos = {variable_uno, variable_dos, variable_tres}

lista_datos = [set_datos, False]

print(f'Lista de datos: {lista_datos}')

# uso de metodos de los set de datos o conjuntos
set_datos.add(5) # agregar un elemento al set

set_datos.remove(8) # elimina un elemento del set
print(set_datos) 

set_datos_copy = set_datos.copy() # copiar el set

set_datos.clear() # limpiar el set
print(set_datos_copy)

set_datos.difference_update({8, 10.5}) # eliminar los elementos que coincidan con el set

interseccion_datos = set_datos.intersection(set_datos_copy) # interseccion de dos sets
print(interseccion_datos)

