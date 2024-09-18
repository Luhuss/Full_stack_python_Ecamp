import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from principal.vehiculo import Vehiculo
from herencia.automovil import Automovil
from herencia.particular import Particular
from herencia.carga import Carga
from herencia.bicicleta import Bicicleta
from herencia.motocicleta import Motocicleta


def crear_vehiculo() -> Vehiculo:
    tipo = input('Seleccione el tipo de vehiculo (automovil, particular, carga, bicicleta, motocicleta)')
    
    if tipo == 'automovil':
        marca = input('Inserte la marca del automovil: ')
        modelo = input('Inserte el modelo: ')
        numero_ruedas = int(input('Inserte el numero de ruedas: '))
        velocidad = input('Inserte la velocidad en km/h: ')
        cilindrada = input('Inserte el cilindraje: ')
        return Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
    
    elif tipo == 'particular':
        marca = input('Inserte la marca del automovil: ')
        modelo = input('Inserte el modelo: ')
        numero_ruedas = int(input('Inserte el numero de ruedas: '))
        velocidad = input('Inserte la velocidad en km/h: ')
        cilindrada = input('Inserte el cilindraje: ')
        numero_asientos = input('Inserte el numero de asientos: ')
        return Particular(marca, modelo, numero_ruedas, velocidad, cilindrada, numero_asientos)
    
    elif tipo == 'carga':
        marca = input('Inserte la marca del automovil: ')
        modelo = input('Inserte el modelo: ')
        numero_ruedas = int(input('Inserte el numero de ruedas: '))
        velocidad = input('Inserte la velocidad en km/h: ')
        cilindrada = input('Inserte el cilindraje: ')
        carga_maxima = input('Inserte el carga maxima: ')
        return Carga(marca, modelo, numero_ruedas, velocidad, cilindrada, carga_maxima)

def imprimir_objetos(lista):
    for i in lista:
        print(i)
        
        
def ingrese_tipo_vehiculo() -> str:
    return str(input('Que tipo de vehiculo desea llamar: '))

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