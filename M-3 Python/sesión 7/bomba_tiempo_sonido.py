'''
Esta versión reproduce un sonido al explotar la bomba. Funciona en Windows con la biblioteca winsound.
'''

import time
# import winsound

def bomba_de_tiempo(tiempo):
    while tiempo > 0:
        print(f"Tiempo restante: {tiempo} segundos")
        time.sleep(1)
        tiempo -= 1

    print("¡Bomba del tiempo a explotar!")
    #winsound.Beep(1000, 500)  # Reproduce un beep al final

# Ejemplo de uso: Cuenta regresiva de 10 segundos
bomba_de_tiempo(10)
