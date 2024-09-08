# tuplas
# Estructura de datos inmutable
# se declaran con ()

tupla_datos = () # tupla vacía
print(type(tupla_datos)) # <class 'tuple'>

tupla_datos = (1, 2, 3, 4, 5) # reasignación de valor
print(tupla_datos) # (1, 2, 3, 4, 5)

cuenta = tupla_datos.count(1)
print(cuenta) # 1

indice_del_valor = tupla_datos.index(5)
print(indice_del_valor) # 4

# contenido = indice_del_valor[0] # TypeError: 'int' object is not subscriptable