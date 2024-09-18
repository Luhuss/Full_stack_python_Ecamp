class Vehiculo:
    def __init__(self, marca :str, modelo :str, numero_ruedas :int) -> None:
        self._marca          = marca
        self._modelo         = modelo
        self._numero_ruedas  = numero_ruedas
        
    @property
    def marca(self) -> str:
        return self._marca
    
    @marca.setter
    def marca(self, marca :str) -> None:
        self._marca = marca
        
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo :str) -> None:
        self._modelo = modelo
        
    @property
    def numero_ruedas(self) -> str:
        return self._numero_ruedas
    
    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas :int) -> None:
        self._numero_ruedas = numero_ruedas 
        
        
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: int, cilindrada: int) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada
        
    @property
    def velocidad(self) -> int:
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad: int) -> None:
        self._velocidad = velocidad
        
    @property
    def cilindrada(self) -> int:
        return self._cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada :int) -> None:
        self._cilindrada = cilindrada
        
    def __str__(self) -> str:
        return f'Datos del automovil: Marca {self._marca}, Modelo {self._modelo}, ruedas{self._numero_ruedas}, velocidad {self._velocidad}, cilindrada {self._cilindrada}'
        
def crear_vehiculo() -> Vehiculo:
    marca = input('Inserte la marca del automovil: ')
    modelo = input('Inserte el modelo: ')
    numero_ruedas = int(input('Inserte el numero de ruedas: '))
    velocidad = input('Inserte la velocidad en km/h: ')
    cilindrada = input('Inserte el cilindraje: ')
    return Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)

def imprimir_objetos(lista):
    for i in lista:
        print(i)
        
def ingrese_cantidad() -> int:
    return int(input('Cuantos vehiculos desde insertar: '))

def orquestacion_creacion() -> list[Automovil]:
    cantidad_ingresos = ingrese_cantidad()
    
    lista_vehiculos = []
    for i in range(0, cantidad_ingresos):
        print('Datos del automovil ', i+1)
        vehiculo = crear_vehiculo()
        lista_vehiculos.append(vehiculo)
    return lista_vehiculos

lista = orquestacion_creacion()
print('Lista de vehiculos: ')
imprimir_objetos(lista)
    
    