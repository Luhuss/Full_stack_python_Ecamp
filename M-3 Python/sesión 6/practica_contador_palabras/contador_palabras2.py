def contar_vocales(cadena):
    contador = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    cadena = cadena.lower()
    for letra in cadena:
        if letra in vocales:
            contador +=1
    return contador

texto = input("Ingresa una cadena de texto: ")
cantidad_vocales = contar_vocales(texto)
print("La cantidad de vocales en la cadena es: ", cantidad_vocales)