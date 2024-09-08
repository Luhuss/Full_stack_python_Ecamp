'''
Dada una lista de diccionarios que representan información de estudiantes, realizar las siguientes tareas:
estudiantes = [
{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
{'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
{'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
{'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
{'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85.
• Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad sea un número primo.
'''

def es_primo(numero):
    # Esta función verifica si un número es primo.
    if numero < 2:
        return False
    for i in range (2, int(numero**0.5) +1):
        if numero % i == 0:
            return False
    return True

def promedio_notas(lista):
    # Esta función calcula el promedio de una lista de calificaciones.
    return sum(lista)/ len(lista)

# Lista de estudiantes con su información
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

# Filtrar y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85.
estudiantes_filtrados = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and promedio_notas(estudiante['calificaciones']) > 85:
        # agregar el estudiante a la lista filtrada
        estudiantes_filtrados.append(estudiante)
        # Imprimir detalles del estudiante filtrado
        print(f'Estudiante: {estudiante['nombre']}')
        print(f'Edad: {estudiante['edad']}')
        print(f' Promedio de calificaciones: {promedio_notas(estudiante['calificaciones'])}\n')
        
# Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad sea un número primo.
for estudiante in estudiantes_filtrados:
    if es_primo(estudiante['edad']):
        print(f'{estudiante['nombre']}')
        print(f'Promedio calificación {promedio_notas(estudiante['calificaciones'])} \n')

    
# Resumen
# Función es_primo: Determina si un número es primo.
# Función promedio_notas: Calcula el promedio de una lista de calificaciones.
# Lista de Estudiantes: Contiene la información de los estudiantes.
# Filtrado: Selecciona estudiantes con más de 18 años y un promedio de calificaciones superior a 85, e imprime sus detalles.
# Cálculo del Promedio para Edad Prima: Calcula y muestra el promedio de calificaciones para aquellos estudiantes cuya edad es un número primo.