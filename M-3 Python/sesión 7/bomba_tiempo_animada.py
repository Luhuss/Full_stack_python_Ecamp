'''
En esta versión, la cuenta regresiva se actualiza en la misma línea usando sys.stdout.write y sys.stdout.flush() para crear una animación simple.
'''

import time
import sys

def bomba_de_tiempo(tiempo):
    while tiempo > 0:
        sys.stdout.write(f"\rTiempo restante: {tiempo} segundos")
        sys.stdout.flush()
        time.sleep(1)
        tiempo -= 1

    print("\n¡Bomba del tiempo a explotar!")

# Ejemplo de uso: Cuenta regresiva de 10 segundos
bomba_de_tiempo(10)
