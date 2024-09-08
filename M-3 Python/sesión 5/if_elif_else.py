# estructuras condicionales, pueden controlar el flujo del aplicativo
# if, elif, else

print('Ingrese un número')
num = input() # input() siempre retorna un string
num = int(num) # convertir el string a entero

if(num > 0):
    print('El número es positivo')
elif(num < 0):
    print('El número es negativo')
else:
    print('El número es cero')
    
# ------------------------ En Python, los paréntesis alrededor de las condiciones no son requeridos, pero se pueden usar.
# La sintaxis correcta es sin paréntesis, y es más común y preferida por la comunidad.
# La indentación es lo más importante en Python para definir bloques de código.
if num > 0:
    print('El número es positivo')
elif(num < 0):
    print('El número es negativo')
else:
    print('El número es cero')

