# Usando un 'for' con 'itertools.count'

import itertools

def suma_numeros():
    suma_total = 0
    
    for _ in itertools.count():
        numero = int(input("Ingresa un número entero positivo (o un número negativo para terminar): "))
        
        if numero < 0:
            break
        suma_total += numero
        
    print(f"La suma total de los números ingresados es: {suma_total}")
    
suma_numeros()

# Explicación:

# itertools.count() crea un contador infinito, que permite usar un bucle for que sigue solicitando números hasta que se ingresa un número negativo.