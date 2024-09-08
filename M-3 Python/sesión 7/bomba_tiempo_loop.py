'''
Esta versión usa un bucle for que va desde tiempo hasta 1.
'''

import time

def bomba_de_tiempo(tiempo):
    for i in range(tiempo, 0, -1):
        print(f"Tiempo restante: {i} segundos")
        time.sleep(1)
    
    print("¡Bomba del tiempo a explotar!")

# Ejemplo de uso: Cuenta regresiva de 10 segundos
bomba_de_tiempo(10)
