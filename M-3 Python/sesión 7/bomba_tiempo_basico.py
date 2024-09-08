'''
Esta versión utiliza time.sleep(1) para pausar la ejecución durante 1 segundo entre cada decremento del tiempo.
'''

import time 

def bomba_de_tiempo(tiempo):
    while tiempo > 0:
        print(f"Tiempo restante: {tiempo} segundos")
        time.sleep(1)
        tiempo -= 1
        
    print("Bomba del tiempo a explotar!")
    
# Ejemplo de uso: Cuenta regresiva de 10 segundos
bomba_de_tiempo(10)