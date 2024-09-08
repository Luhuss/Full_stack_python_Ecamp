def suma_numeros():
    suma_total = 0
    
    while True:
        numero = int(input("Ingresa un número entero positivo (o un número negativo para terminar): "))
    
        if numero < 0:
            break
        else:
            suma_total += numero
            
    print(f"La suma total de los números ingresados es: {suma_total}")
    
suma_numeros()


# Cómo funciona:
# Inicialización: La variable suma_total se inicializa en 0 para almacenar la suma de los números ingresados.

# Bucle while: El programa entra en un bucle infinito que solo se detiene cuando el usuario ingresa un número negativo.

# Entrada del usuario: El usuario ingresa un número entero positivo.

# Condición de parada: Si el número ingresado es negativo, el bucle se rompe con break, deteniendo la entrada de más números.

# Suma de números: Si el número es positivo, se agrega a suma_total.

# Resultado final: Al salir del bucle, se imprime la suma total de los números ingresados.

# Este programa seguirá pidiendo números hasta que se ingrese un número negativo, y luego mostrará la suma de todos los números positivos ingresados.





