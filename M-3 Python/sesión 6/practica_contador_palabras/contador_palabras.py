def contar_vocales(texto):
    # Definir las vocales
    vocales = "aeiou"
    
    # Convertir el texto a minúsculas para hacerlo insensible a mayúsculas/minúsculas
    texto = texto.lower()
    
    # Inicializar el contador de vocales
    contador_vocales = 0
    
    # Recorrer cada carácter en el texto
    for letra in texto:
        # Verificar si el carácter es una vocal
        if letra in vocales:
            contador_vocales += 1
    
    return contador_vocales

# Solicitar al usuario que ingrese una cadena de texto
texto_usuario = input("Ingresa una cadena de texto: ")

# Contar el número de vocales en el texto ingresado
numero_vocales = contar_vocales(texto_usuario)

# Mostrar el resultado
print(f"El número de vocales en el texto es: {numero_vocales}")
