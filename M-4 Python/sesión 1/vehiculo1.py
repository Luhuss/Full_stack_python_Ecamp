class Vehiculo:
    def __init__(self, marca: str = None, año: str = None, color: str = None, modelo: str = None, 
                peso: float = None, ancho: float = None, alto: float = None):
        self.marca = marca
        self.año = año
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        
    def arrancar(self):
        print(f'El vehículo {self.marca} {self.modelo} arrancó')
        
    def frenar(self):
        print(f'El vehículo {self.marca} {self.modelo} frena')
    
    def girar_izquierda(self):
        print(f'El vehículo {self.marca} {self.modelo} gira a la izquierda')
        
    def girar_derecha(self):
        print(f'El vehículo {self.marca} {self.modelo} gira a la derecha')
        
    def apagar(self):
        print(f'El vehículo {self.marca} {self.modelo} apagado')
        
    def encender(self):
        print(f'El vehículo {self.marca} {self.modelo} encendido')
        
    def retroceder(self):
        print(f'El vehículo {self.marca} {self.modelo} retrocede')
        
    def derrapar(self):
        print(f'El vehículo {self.marca} {self.modelo} derrapa')
    
    def __str__(self) -> str:
        return (f'Vehículo[marca: {self.marca}, año: {self.año}, color: {self.color}, '
                f'modelo: {self.modelo}, peso: {self.peso}kg, ancho: {self.ancho}m, alto: {self.alto}m]')


# Instancias de Vehiculo usando el constructor con parámetros
vehiculo_uno = Vehiculo('Porche', '1964', 'Plateado', '911 1964', 1.080, 1.61, 1.32)
vehiculo_dos = Vehiculo('Ford', '1965', 'Rojo', 'Mustang', 1.365, 1.73, 1.32)
vehiculo_tres = Vehiculo('Chevrolet', '1957', 'Azul', 'Bel Air', 1.625, 1.95, 1.49)
vehiculo_cuatro = Vehiculo('Cadillac', '1959', 'Negro', 'El Dorado', 2.255, 2.03, 1.41)

# Instancia de Vehiculo usando el constructor sin parámetros
vehiculo_cinco = Vehiculo()
vehiculo_cinco.marca = 'Chevrolet'
vehiculo_cinco.año = '2010'
vehiculo_cinco.color = 'Negro'
vehiculo_cinco.modelo = 'Aveo'
vehiculo_cinco.peso = 1500
vehiculo_cinco.ancho = 2
vehiculo_cinco.alto = 1.5

# Instancia de Vehiculo usando el constructor sin parámetros
vehiculo_seis = Vehiculo()
vehiculo_seis.marca = 'Volkswagen'
vehiculo_seis.año = '1967'
vehiculo_seis.color = 'Blanco'
vehiculo_seis.modelo = 'Beetle'
vehiculo_seis.peso = 840
vehiculo_seis.ancho = 1.55
vehiculo_seis.alto = 1.50

# Ejemplo de uso de los métodos
vehiculo_uno.encender()
vehiculo_uno.arrancar()
vehiculo_uno.girar_izquierda()
vehiculo_uno.girar_derecha()
vehiculo_uno.derrapar()
vehiculo_uno.retroceder()
vehiculo_uno.apagar()

# Impresión de los objetos
print(vehiculo_uno)
print(vehiculo_dos)
print(vehiculo_tres)
print(vehiculo_cuatro)
print(vehiculo_cinco)
print(vehiculo_seis)
