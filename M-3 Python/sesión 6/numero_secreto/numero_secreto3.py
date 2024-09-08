import random

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = []

    while True:
        numero_ingresado = int(input("Adivina el número (entre 1 y 100): "))
        intentos.append(numero_ingresado)

        if numero_ingresado < numero_aleatorio:
            print("Demasiado bajo.")
        elif numero_ingresado > numero_aleatorio:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {len(intentos)} intentos.")
            print(f"Intentos anteriores: {intentos}")
            break

adivinar_numero()
