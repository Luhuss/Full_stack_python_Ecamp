# declarar variables
a = 20
b = 30

#operación realizada
c = a * b

print(c)
print("El resultado de la multiplicación es: ", c)
print(f'El resultado de la multiplicación es: {c}')
print(f'El resultado de multiplicar {a} y {b} es: {c}')
print('El resultado de multiplicar {} y {} es: {}' .format(a, b, c))
# print('El resultado de la multiplicación es: ' + c)  TypeError: can only concatenate str (not "int") to str