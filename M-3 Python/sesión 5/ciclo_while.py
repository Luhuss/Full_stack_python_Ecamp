# ciclo while, mientras que
# while condicion: 

# i, j, k, temp, iterador,  nombre para los iteradores

i = 0
while i < 5:
    i += 1 # aumenta el valor del iterador, para controlar el ciclo
    print(i)
    
i = 0
while i < 5:
    print(i)
    i += 1 # aumenta el valor del iterador, para controlar el ciclo
    
i = 0
while i < 5:
    print(i)
    i += 1 # aumenta el valor del iterador, para controlar el ciclo
    if i == 1:
        continue # salta a la siguiente iteracion
    print(f'Imprimiendo el valor de {i}')

i = 0
while i < 5:
    print(i)
    i += 1 # aumenta el valor del iterador, para controlar el ciclo
    if i == 1:
        break # salta a la siguiente iteracion
    print(f'Imprimiendo el valor de {i}')