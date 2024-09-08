import random

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 4 # Número maximo de intentos
    
    for intento in range(1, intentos + 1):
        numero_ingresado = int(input(f"intento {intento}/{intentos}. Adivina el número (entre 1 y 100): "))
        
        if numero_ingresado < numero_aleatorio:
            print("Demasiado bajo.")
        elif numero_ingresado > numero_aleatorio:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste. El número era {numero_aleatorio}.")
        
adivinar_numero()