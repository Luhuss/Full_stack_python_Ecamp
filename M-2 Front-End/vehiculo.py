class Vehiculo:
    def __init__(self, color, aceleracion):
        self.color          = color
        self.aceleracion    = aceleracion
        self.velocidad      = 0
        
    def set_color(self, color):
        self.color          = color
            
    def get_color(self):
        return self.color
    
miCarro1 = Vehiculo('Negro', '20')
print(miCarro1.get_color())
miCarro1.set_color('Blanco')
print(miCarro1.get_color())

print('----------------------------------------------------------')

class Vehiculo_1:
    def __init__(self, marca, color, ruedas):
        self.marca      = marca
        self.color      = color
        self.ruedas     = ruedas
        
class datosVehiculo_1:
    def __init__(self):
        self.vehiculo_1 = Vehiculo_1('Toyota', 'Rojo', 4)
        print('Datos del Vehiculo:')
        print('Marca: ', self.vehiculo_1.marca)
        print('Color: ', self.vehiculo_1.color)
        print('Ruedas: ', self.vehiculo_1.ruedas)
        
carro = datosVehiculo_1()

print('----------------------------------------------------------')

class Componente:
    def __init__(self):
        print('Objeto de la clase componente ha sido creado')
    def metodo_1(self):
        print('Se ejecuta el metodo_1() de la clase Componente')
        
class Composicion:
    def __init__(self):
        self.objeto_1 = Componente()
        print('Objeto de la clase Composición ha sido creado')
    def metodo_2(self):
        print('Se ejecuta el metodo_2() de la clase Composición')
        self.objeto_1.metodo_1()
        
objeto_2 = Composicion()
objeto_2.metodo_2()

print('----------------------------------------------------------')

#def product(a, b):
#    p = a * b
#    print(p)
    
def product(a, b, c):
    p = a * b * c
    print(p)
    
product(4, 5, 5)

print('----------------------------------------------------------')

def add(datatype, *args):
    if datatype == 'int':
        answer = 0
    elif datatype == 'str':
        answer = ''
    for x in args:
        answer = answer + x
        
    print(answer)   
        
add('int', 5, 6)
add('str', 'Hola')
        
print('----------------------------------------------------------')

from multipledispatch import dispatch

# Definición de product para dos enteros
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)

# Definición de product para tres enteros
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# Definición de product para tres floats
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)

# Ejemplos de uso:
product(2, 3, 2)          # Llama a la versión con tres enteros, imprime 12
product(2.2, 3.4, 2.3)    # Llama a la versión con tres floats, imprime 17.204
