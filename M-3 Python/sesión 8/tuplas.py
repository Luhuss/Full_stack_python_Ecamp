'''
Son colecciones de datos que se pueden modificar
El acceso a los elementos de una tupla es por indice 
Se define con parentesis ()
Se pueden definir con la funcion tuple()
'''

tupla = tuple()  # Creación de una tupla vacía utilizando la función `tuple()`.
tupla = ()  # Creación de una tupla vacía utilizando paréntesis `()`.
num = 1,2,3,4,5  # Creación de una tupla de números sin paréntesis explícitos.
print(tupla)  # Imprime la tupla vacía `()`.
print(num)  # Imprime la tupla `num`, que contiene los números (1, 2, 3, 4, 5).

#Tuplas: Son colecciones ordenadas de elementos que no se pueden modificar después de su creación. Se pueden definir con paréntesis () o usando la función tuple().

# indices van desde 0 a n-1
tupla = (40, 1.80, 'Fulanito', ' Perez') # Creación de una tupla con elementos de diferentes tipos.

# acceder a la longitud de la tupla
print('La longitud de la tupla es', len(tupla)) # Muestra la cantidad de elementos en la tupla.

# acceder a un elemento mediante el indice
print('El primer elemento es', tupla[0]) # Accede al primer elemento (40).
print('El ultimo elemento es', tupla[-1]) # Accede al último elemento (' Perez').
# len(): Retorna el número de elementos en la tupla.
# Índices: Se usan para acceder a elementos específicos de la tupla. Los índices comienzan en 0 y pueden ser negativos para acceder desde el final.

# contar elementos existentes en un tupla
print('Elementos numero 40 existentes', tupla.count(40)) # Cuenta cuántas veces aparece el número 40 en la tupla.
# count(): Devuelve el número de veces que un valor aparece en la tupla.

# obtener el indice de un elemento
print('El indice del elemento 40', tupla.index(40)) # 1 # Encuentra el índice de la primera aparición de 40.
# index(): Devuelve el índice de la primera aparición de un valor en la tupla.

# desempaquetar tuplas
# Genera error ValueError: too many values to unpack, si existen menos o mas elementos que variables
a, b, c, d, e = num # Desempaqueta los valores de la tupla `num` en variables individuales.

# a = num[0]
print(f'a:{a}, b:{b}') # Imprime los valores de `a` y `b`.
# Desempaquetado: Asigna los elementos de una tupla a variables individuales. La cantidad de variables debe coincidir con la cantidad de elementos en la tupla.

# crear una tupla de otra tupla
# otra tupla = tupla
            # (40, 1.80, 'Fulanito), 'Perez')
sub_tupla = tupla [0:3] # Crea una sub-tupla desde el índice 0 hasta el 2 (exclusivo).
print('Sub tupla', sub_tupla) # Imprime la sub-tupla (40, 1.80, 'Fulanito').
print(tupla[2: ]) # Crea una sub-tupla desde el índice 2 hasta el final ('Fulanito', ' Perez').
print(tupla[:-1]) # Crea una sub-tupla desde el principio hasta el penúltimo elemento (40, 1.80, 'Fulanito').
print(tupla[0:4:2]) # Crea una sub-tupla desde el índice 0 hasta el 3, con saltos de 2 en 2 (40, 'Fulanito').
# Sub-tuplas: Se crean utilizando la notación de slicing [inicio:fin:paso]

# [inicio:final:paso]
# (inicio:final:paso)
# [inicio:fin]: Incluye desde el índice inicio hasta fin-1.
# [inicio:fin:paso]: Incluye desde el índice inicio hasta fin-1, tomando elementos cada paso.


# Resumen:
# Inmutabilidad: Las tuplas no pueden modificarse después de ser creadas.
# Índices: Se usan para acceder a elementos en una tupla, comenzando desde 0.
# Slicing: Permite crear sub-tuplas o acceder a segmentos específicos de una tupla.
# Desempaquetado: Permite asignar elementos de una tupla a variables individuales.


