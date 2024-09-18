def pedir_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            return edad
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            
def verificar_adulto(edad):
    if edad >= 18:
        print("Es un adulto.")
    else:
        print("No es un adulto.")
        
edad = pedir_edad()
verificar_adulto(edad)