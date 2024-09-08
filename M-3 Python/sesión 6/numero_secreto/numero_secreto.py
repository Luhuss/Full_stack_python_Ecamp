import random

def adivinar_numero():
    # genera un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1,100)
    intentos = 0
    
    while True:
        #Pedir al usuario que ingrese un número
        intento = int(input("Adivina el númro (enre 1 y 100): "))
        intentos +=1
        
        #comparar el número ingresado con el número aleatorio
        if intento < numero_aleatorio:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_aleatorio:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
            break
        
# Llamar a la función para iniciar el juego
adivinar_numero()

# Explicación:
# random.randint(1, 100): Genera un número aleatorio entre 1 y 100.
# int(input("Adivina el número (entre 1 y 100): ")): Solicita al usuario que ingrese un número y lo convierte a un entero.
# Bucles y Condicionales:
# El programa utiliza un bucle while que continuará ejecutándose hasta que el usuario adivine el número correctamente.
# Si el número ingresado es menor que el número generado, el programa informa que es "Demasiado bajo".
# Si es mayor, informa que es "Demasiado alto".
# Cuando el número es correcto, se rompe el bucle y se felicita al usuario, indicando cuántos intentos necesitó.
