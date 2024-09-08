'''
Los objetos comienzan con la palabra class, inician con el nombre del objeto en mayuscula
Los objetos tienen constructor(crear la instancia) y accesadores.
'''
#class nombre_objeto:
class Vehiculo:
    # constructor con parametros, se necesitan todos los atributos o parametros para instanciar al objeto
    def __init__(self, marca, año, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.año = año
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    # constructor vacio o construcor sin parametros, se pueden omitir los atributos
    def __init__(self, marca=None, año=None, color=None, modelo=None, peso=None, ancho=None, alto=None):
        self.marca = marca
        self.año = año
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        
    def arrancar(self):
        print(f'El vehiculo {self.marca} {self.modelo} arranco')
        
    def frenar(self):
        print(f'El vehiculo {self.marca} {self.modelo} frena')
    
    def girar_izquierda(self):
        print(f'El vehiculo {self.marca} {self.modelo} gira a la izquierda')
        
    def girar_derecha(self):
        print(f'El vehiculo {self.marca} {self.modelo} gira a la derecha')
        
    def apagar(self):
        print(f'El vehiculo {self.marca} {self.modelo} apaga')
        
    def encender(self):
        print(f'El vehiculo {self.marca} {self.modelo} encendido')
        
    def retroceder(self):
        print(f'El vehiculo {self.marca} {self.modelo} retrocede')
    
    # funcion para imprimir los objetos en String y no la referencia en memoria del objeto    
    def __str__(self) -> str:
        return f'Vehiculo[ marca:{self.marca}, año:{self.año}, color:{self.color}, modelo:{self.modelo}, peso:{self.peso}, ancho:{self.ancho}, alto:{self.alto}'    


# instancia de Vehiculo invocando al constructor con parametros        
vehiculo = Vehiculo('BMW', '2023','Blanco', 'M3', '1500', '2', '1.5')
vehiculo.color = 'Rojo'

vehiculo_uno = Vehiculo('Porche', '1964', 'Plateado', '911 1965', 1.080, 1.61, 1.32)
vehiculo_dos = Vehiculo('Ford', '1965','Rojo', 'Mustang', 1365, 1.73, 1.32)
vehiculo_tres = Vehiculo('Chevrolet', '1957', 'Azul', 'Bel Air', 1.625, 1.95, 1.49)
vehiculo_cuatro = Vehiculo('Cadillac', '1959', 'Negro', 'El Dorado', 2.255, 2.03, 1.41)

'''
# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_uno = Vehiculo()
vehiculo_uno.marca = 'Chevrolet' # asignando los atributos del objeto
vehiculo_uno.año = '2010'        # asignando los atributos del objeto
vehiculo_uno.color = 'Negro'     # asignando los atributos del objeto
vehiculo_uno.modelo = 'Aveo'     # asignando los atributos del objeto
vehiculo_uno.peso = '1500'       # asignando los atributos del objeto
vehiculo_uno.ancho = '2'         # asignando los atributos del objeto
'''
# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_cinco = Vehiculo()
vehiculo_cinco.marca = 'Chevrolet' # asignando los atributos del objeto
vehiculo_cinco.año = '2010'        # asignando los atributos del objeto
vehiculo_cinco.color = 'Negro'     # asignando los atributos del objeto
vehiculo_cinco.modelo = 'Aveo'     # asignando los atributos del objeto
vehiculo_cinco.peso = '1500'       # asignando los atributos del objeto
vehiculo_cinco.ancho = '2'         # asignando los atributos del objeto

# instancia de Vehiculo invocando al constructor con parametros
# class Vehiculo(
#     marca: Any  | None = None,
#     año: Any    | None = None,
#     color: Any  | None = None,
#     modelo: Any | None = None,
#     peso: Any   | None = None,
#     ancho: Any  | None = None,
#     alto: Any   | None = None
# )     


# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_seis = Vehiculo()
vehiculo_seis.marca  = 'Chery' # asignando los atributos del objeto


# invocando metodos del objeto, accediendo a los métodos del objeto
vehiculo.encender()
vehiculo.arrancar()
vehiculo.girar_izquierda()
vehiculo.girar_derecha()
vehiculo.retroceder()
print('---------------------------------------------')
vehiculo_cinco.encender()

# impresión del objeto, usara la funcion def __str__ definida dentro del objeto
# print(vehiculo)
print(vehiculo_uno)
print(vehiculo_dos)
print(vehiculo_tres)
print(vehiculo_cuatro)
print(vehiculo_cinco)
