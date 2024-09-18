
def division():
    suma = 3000
    contador = 0

    try:
    
        resultado = suma/contador
    
    except ZeroDivisionError as e:
    
        print(e)
division()