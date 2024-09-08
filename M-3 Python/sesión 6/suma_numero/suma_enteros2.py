# Usando un 'while' con 'try' y 'except' 

def suma_numeros():
    suma_total = 0
    
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo (o un número negativo para terminar): "))
            if numero < 0:
                break
            suma_total += numero
        except ValueError:
            print("Por favor, ingresa un número válido.")
        
    print(f"La suma total de los números ingresados es: {suma_total}")
    
suma_numeros()

# Explicación:

# Este enfoque agrega manejo de excepciones para asegurarse de que el usuario ingrese un número entero válido. Si se ingresa algo que no es un número, el programa mostrará un mensaje de error y pedirá de nuevo el número.