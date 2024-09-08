'''
Set, conjunto de datos
no permite elementos repetidos
no mantiene un orden 
se definen mediante la funcion set()
se define con llaves
'''

mi_set = {} # Esto en realidad crea un diccionario vacío, no un set.
mi_set = set({1,2,3,4,5,6,7}) # Crea un set con elementos únicos.
print(mi_set) # {1, 2, 3, 4, 5, 6, 7}


# Sets: Son colecciones de elementos no ordenados y únicos. Si se intenta agregar elementos duplicados, el set los eliminará automáticamente.
# Definición de sets: Se pueden definir utilizando la función set() o con llaves {}. Nota que {} sin elementos crea un diccionario, no un set.


# longitud de un set
print('La longitud del conjunto es', len(mi_set)) # Muestra el número de elementos únicos en el set.
# len(): Retorna el número de elementos en el set.

# agregar un elemento al set
mi_set.add(8) # añade el elemento 8
# add(): Añade un elemento al set. Si el elemento ya existe, no se añade de nuevo.

# eliminar un elemento si existe
# mi_set.remove(10) # Elimina el elemento 10 si existe; si no, arroja un error `KeyError`.
mi_set.discard(2) # Elimina el elemento 2 si existe; si no, no hace nada.
# remove(): Elimina un elemento específico del set. Si el elemento no existe, arroja un error KeyError.
# discard(): Elimina un elemento del set si existe; si no, no arroja error.

copy_mi_set = mi_set.copy() # Crea una copia del set original.
print('La copia del conjunto es', copy_mi_set)
# copy(): Crea una copia del set original.

# ordenar un set
mi_set_ordenado = set(sorted(mi_set)) # Ordena los elementos del set.
print('El conjunto ordenado es', mi_set_ordenado)
# sorted(): Ordena los elementos del set y retorna una lista. Para mantenerlo como un set, se convierte nuevamente usando set().

# eliminar todos los elementos
copy_mi_set.clear() # elimina todos los elementos del set
print('La copia del conjunto es', copy_mi_set)
# clear(): Elimina todos los elementos del set, dejándolo vacío.

# añadir un elemento 
copy_mi_set.add('un elemento agregado') # Añade un elemento al set.
print('La copia del conjunto es', copy_mi_set)

# eliminar un elemento
copy_mi_set.remove('Un elemento agregado') # Elimina el elemento si existe; si no, arroja un error `KeyError`.

# Actualizar el set con nuevos elementos
copy_mi_set.update({'otra vez'}) # añade otro elemento al set
print('La copia del conjunto es', copy_mi_set)
# update(): Añade múltiples elementos al set.

# Unión de sets
print('La union de los set es', mi_set_ordenado.union(copy_mi_set)) # union de los dos sets
# union(): Retorna un nuevo set con todos los elementos de ambos sets, sin duplicados.

# Intersección de sets
set_interseccion = mi_set.intersection({1,2}) # interseccion de los dos sets
print('La interseccion de los set es', set_interseccion)
# intersection(): Retorna un nuevo set con los elementos comunes en ambos sets.

mi_set.intersection_update(copy_mi_set) # Actualiza el set original con la intersección.
print('El conjunto mi_set ahora es', mi_set)
# intersection_update(): Actualiza el set original, conservando solo los elementos comunes con otro set.

# desempaquetar set
a = set_interseccion # Desempaqueta la intersección en una variable.
print(f'a:{a}') # Imprime la intersección.
# Desempaquetado: Asigna el set o su contenido a una variable.

# Resumen:
# Sets: Son colecciones de datos no ordenados que no permiten elementos duplicados.
# Operaciones comunes: Se pueden agregar, eliminar, copiar, y combinar sets usando varias funciones integradas.
# Operaciones de conjunto: Como unión e intersección, permiten trabajar con varios sets a la vez.
