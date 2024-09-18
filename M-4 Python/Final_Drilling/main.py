import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Final_Drilling.vehiculo import Vehiculo
from Final_Drilling.vehiculo import Automovil
from Final_Drilling.tipo_vehiculo import Particular
from Final_Drilling.tipo_vehiculo import Carga
from Final_Drilling.tipo_vehiculo import Bicicleta
from Final_Drilling.tipo_vehiculo import Motocicleta

def guardar(self, nombre_archivo: str) -> None:
    try:
        with open(nombre_archivo, "a", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            datos = [self.__class__.__name__, self._marca, self._modelo, self._numero_ruedas]
            archivo_csv.writerow(datos)
    except Exception as e:
        print(f"Error al guardar en el archivo CSV: {e}")

@staticmethod
def recuperar(nombre_archivo: str):
    objetos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for fila in archivo_csv:
                objetos.append(fila)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return objetos  

def crear_vehiculo() -> Automovil:
    marca = input('Inserte la marca del automovil: ')
    modelo = input('Inserte el modelo: ')
    numero_ruedas = int(input('Inserte el numero de ruedas: '))
    velocidad = int(input('Ingrese la velocidad en km/h: '))
    cilindrada = int(input('Ingrese el cilindraje: '))
    return Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)

def imprimir_objetos(lista):
    for i in lista:
        print(i)
        
def ingrese_cantidad() -> int:
    return int(input('Cuantos vehiculos desea insertar: '))

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

particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print('Motocicleta es instancia con relación a Vehículo:', isinstance(motocicleta, Vehiculo))
print('Motocicleta es instancia con relación a Automovil:', isinstance(motocicleta, Automovil))
print('Motocicleta es instancia con relación a Vehículo particular:', isinstance(motocicleta, Particular))
print('Motocicleta es instancia con relación a Vehículo de Carga:', isinstance(motocicleta, Carga))
print('Motocicleta es instancia con relación a Bicicleta:', isinstance(motocicleta, Bicicleta))
print('Motocicleta es instancia con relación a Motocicleta:', isinstance(motocicleta, Motocicleta))