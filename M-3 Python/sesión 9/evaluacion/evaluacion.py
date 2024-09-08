'''
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente.
'''

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def operaciones(a, b):
    # Crear una tupla con los resultados de las operaciones
    resultados = (
        sumar(a, b),
        restar(a, b),
        multiplicar(a, b),
        dividir(a, b)
    )

    # Crear un diccionario para almacenar los resultados
    resultados_diccionario = {
        "Suma": resultados[0],
        "Resta": resultados[1],
        "Multiplicación": resultados[2],
        "División": resultados[3]
    }

    return resultados_diccionario

# Ejemplo de uso:
a = 10
b = 5
resultados = operaciones(a, b)
print(resultados)

