import random

def adivinar_numero(numero_aleatorio, intentos=1):
    numero_ingresado = int(input("Adivina el número (entre 1 y 100): "))

    if numero_ingresado < numero_aleatorio:
        print("Demasiado bajo.")
        adivinar_numero(numero_aleatorio, intentos + 1)
    elif numero_ingresado > numero_aleatorio:
        print("Demasiado alto.")
        adivinar_numero(numero_aleatorio, intentos + 1)
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")

numero_aleatorio = random.randint(1, 100)
adivinar_numero(numero_aleatorio)
