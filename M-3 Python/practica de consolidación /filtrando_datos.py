# Lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Lista para separar los nombres
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []

# Función para añadir 'El gran' a los nombres de magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = f"El gran {magos[i]}"

# Función para imprimir los nombres
def imprimir_nombres(lista, titulo):
    print(titulo)
    for nombre in lista:
        print(nombre)
    print()


# Separar los nombres en las listas
for nombre in nombres:
    if nombre in magos:
        continue
    elif nombre in cientificos:
        continue
    else:
        otros.append(nombre)

# Imprimir la lista de nombres 
imprimir_nombres(nombres, "Lista original de nombres:")

# Hacer grandiosos a los magos
hacer_grandioso(magos)

# Imprimir las lista de nombres
imprimir_nombres(magos, "Magos grandiosos:")
imprimir_nombres(cientificos, "Cientificos:")
imprimir_nombres(otros, "Otros:")
