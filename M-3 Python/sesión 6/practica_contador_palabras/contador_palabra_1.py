# ingreso de cadena
texto = input("Ingresa una cadena de texto: ")

# Convertir el texto a minúsculas para que comparacioón sea insecible a mayúsculas/minúsculas
texto = texto.lower()

# Definir un conjunto de vocales
vocales = "aeiou"

# Inicializar un contador de vocales
contador_vocales = 0

# Recorre cada letra en la cadena de texto
for letra in texto:
    if letra in vocales:
        contador_vocales +=1
        
# Imprimir el resultado
print(f"la cantidad de vocales en la cadena de texto es: {contador_vocales}")