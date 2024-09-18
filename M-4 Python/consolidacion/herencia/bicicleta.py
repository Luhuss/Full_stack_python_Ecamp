import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from principal.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo: str) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self._tipo = tipo
        
    @property
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo: str) -> None:
        self._tipo = tipo
        
    def __str__(self) -> str:
        return (f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, "
                f"Tipo: {self.tipo}")