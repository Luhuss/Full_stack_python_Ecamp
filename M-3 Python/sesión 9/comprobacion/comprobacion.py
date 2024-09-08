'''
Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo.
Validar que ambos sean números positivos.
'''

def calcular_area_rectangulo(base, altura):
    # Validar que ambos parámetros sean números positivos
    if isinstance(base, (int, float)) and isinstance(altura, (int, float)):
        if base > 0 and altura > 0:
            area = base * altura
            return area
        else:
            return "Error: La base y la altura deben ser números positivos."
    else:
        return "Error: Ambos parámetros deben ser números."

# Ejemplo de uso:
base = 5
altura = 10
resultado = calcular_area_rectangulo(base, altura)
print("El área del rectángulo es:", resultado)
