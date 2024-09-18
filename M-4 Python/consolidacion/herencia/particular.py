import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from herencia.automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: int, cilindrada: int, numero_asientos: str) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._numero_asientos = numero_asientos
        
    @property
    def numero_asientos(self) -> str:
        return self._numero_asientos
    
    @numero_asientos.setter
    def numero_asientos(self, numero_asientos: str) -> None:
        self._numero_asientos = numero_asientos
        
    def __str__(self) -> str:
        return (f"Datos del automovil: Marca {self._marca}, Modelo {self._modelo} ruedas {self._numero_ruedas} velocidad {self._velocidad} km/h, cilindrada {self._cilindrada} cc, numero_asientos{self._numero_asientos}")
