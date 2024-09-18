import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from herencia.automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: int, cilindrada: int, carga_maxima: int) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._carga_maxima = carga_maxima
        
    @property
    def carga_maxima(self) -> int:
        return self._carga_maxima
    
    @carga_maxima.setter
    def carga_maxima(self, carga_maxima: int) -> None:
        self._carga_maxima = carga_maxima
    
    def __str__(self) -> str:
        return (f"Datos del automovil: Marca {self._marca}, Modelo {self._modelo} ruedas {self._numero_ruedas} velocidad {self._velocidad} km/h, cilindrada {self._cilindrada} cc, carga_maxima{self._carga_maxima}")