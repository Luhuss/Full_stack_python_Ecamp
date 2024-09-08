'''
lista, colecciones de datos
lista, tambien llamadas arreglos, son conjuntos ordenados de elementos.
se definen [] con corchetes
se definen con la funcion list()
'''

lista = [1, 2, 3, 4, 5, 6] # Definición de una lista con elementos. indices van desde 0 a n-1
otra_lista = [] # Creacion de una lista vacia
otra_lista = list() # Creación de una lista vacía utilizando la función `list()`.
otra_lista = [40, 1.80, 'Fulanito', 'Perez'] # lista de diferentes tipos de datos

'''
Listas: Son estructuras de datos ordenadas que pueden contener elementos de cualquier tipo.
Listas vacías: Se pueden crear utilizando corchetes [] o la función list().
'''

# acceder a la longitud de la lista
print('La longitud de la lista es ', len(lista)) # Longitud de `lista`.
print('La longitud de la lista es ', len(otra_lista)) # Longitud de `otra_lista`.
# len(): Retorna la cantidad de elementos en una lista.

# conocer el tipo de dato
print(type(lista)) # Muestra que el tipo de dato de `lista` es `<class 'list'>`.
# type(): Devuelve el tipo de dato del objeto.

# acceder a los elementos de la lista
print('El elemento dentro del indice 0 es ', lista[0]) # Accede al primer elemento.
print('El elemento dentro del indice -1 es', otra_lista[-1]) # # Accede al último elemento. 'Perez'
# Índices: Se utilizan para acceder a los elementos de una lista, comenzando desde 0. Los índices negativos comienzan desde el final de la lista.

# agregar elemento al final de la lista
lista.append(7) # agregar un elemento al final de la lista ( Agrega el número 7 al final de la lista `lista`.)
print('Elementos que se encuentran en la lista', lista) # [1, 2, 3, 4, 5, 6, 7]
# append(): Añade un elemento al final de la lista.

# contar un elemento existente dado en la lista
print('La cuenta de elementos numero 3 existente es ', lista.count(3)) # Cuenta cuántas veces aparece el número 3.
# count(): Devuelve el número de veces que un valor aparece en la lista.

print('El indice de Perez es', otra_lista.index('Perez')) # Encuentra el índice del elemento 'Perez'.
# index(): Devuelve el índice de la primera aparición del valor especificado.

# insertar un elemento en la lista en un indice dado
lista.insert(6, 8) # Inserta el número 8 en el índice 6.
print('Elementos que se encuentran en la lista', lista)  # Muestra la lista actualizada. [1, 2, 3, 4, 5, 6, 8, 7]
lista.insert(-2, 7) # Insertar el número 7 en el penúltimo índice
lista.insert(-1, 8) # Insertar el número 8 en el último índice
print('Elemenstos que se encuentren en la lista', lista) # Muestra la lista actualizada.
# insert(): Inserta un elemento en un índice específico.

# eliminar un elemento en la lista
lista.remove(8) # Remueve la primera aparición del número 8 en `lista`.
print('Elementos que se encuentren en la lista', lista) # Muestra la lista actualizada.
# remove(): Elimina la primera aparición del valor especificado.

suma_lista = lista + otra_lista # Combina `lista` y `otra_lista`.
print(suma_lista) # Muestra la lista combinada.
# Operador +: Se utiliza para concatenar dos listas.

# reversar la lista
lista.reverse() # Invierte el orden de los elementos en `lista`.
print('La lista invertida es', lista) # Muestra la lista invertida.

# ordenar la lista
lista.sort() # Ordena `lista` en orden ascendente.
print('La lista ordenada es', lista) # Muestra la lista ordenada.
lista.sort(reverse=True) # reverse=True # Ordena `lista` en orden descendente.

lista_ordenada = sorted(lista) # Retorna una nueva lista ordenada.
print('La lista ordenada es', lista_ordenada) # Muestra la nueva lista ordenada.
# reverse(): Invierte el orden de los elementos de la lista.
# sort(): Ordena la lista. El argumento reverse=True invierte el orden de ordenación.
# sorted(): Devuelve una nueva lista ordenada sin modificar la lista original.


# desempaquetar una lista, tiene que ser la misma cantidad de variables que elementos de la lista
# Genera error ValueError: too many values to unpack, si existen menos o mas elementos que variables
edad, altura, nombre, apellido = otra_lista # [40, 1.80, 'Fulanito', 'Perez'] # Desempaqueta los elementos de `otra_lista`.
# Desempaquetado: Asigna los elementos de una lista a variables individuales. La cantidad de variables debe coincidir con la cantidad de elementos en la lista.

# edad = otra_lista[0]
print('La edad es', edad)
print('La altura es', altura)
print('El nombre es', nombre)
print('El apellido es', apellido)