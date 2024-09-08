'''
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es: 1 mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
'''

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# 1. Eliminar los elementos duplicados convirtiendo la lista en un set
mi_lista_sin_duplicados = list(set(mi_lista))

# 2. Ordenar la lista resultante en orden ascendente
mi_lista_sin_duplicados.sort()

# Imprimir la lista final
print(mi_lista_sin_duplicados)
