'''
Esta versión permite que el usuario detenga la bomba presionando Ctrl+C, lo que genera una excepción KeyboardInterrupt.

Cada una de estas versiones tiene un enfoque diferente, así que puedes elegir la que mejor se adapte a lo que buscas.
'''

import time

def bomba_de_tiempo(tiempo):
    try:
        while tiempo > 0:
            print(f"Tiempo restante: {tiempo} segundos")
            time.sleep(1)
            tiempo -= 1

        print("¡Bomba del tiempo a explotar!")
    except KeyboardInterrupt:
        print("\nBomba desactivada por el usuario.")

# Ejemplo de uso: Cuenta regresiva de 10 segundos
bomba_de_tiempo(10)
