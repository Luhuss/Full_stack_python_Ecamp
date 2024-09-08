'''
escribre un programa que permita la simulación de una bomba de tiempo. Al ejecutar el programa, se imprimirá el mensaje "Bomba del tiempo a explotar"
'''
import time

i = 5
while i >= 0 :
    print(i)
    i -=1
    time.sleep(1)
    
print('boom')