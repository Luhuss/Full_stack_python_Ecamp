# usando recursividad

def suma_numeros(suma_total = 0):
    numero = int(input("Ingresa un número entero positivo (o un número negativo para terminar): "))
    
    if numero < 0:
        print(f"La suma total de los números ingresados es: {suma_total}")
    else:
        suma_total += numero 
        suma_numeros(suma_total)
        
suma_numeros()
