import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from herencia.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo: str, numero_radios: int, cuadro: str, motor: str) -> None:
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self._numero_radios = numero_radios
        self._cuadro = cuadro
        self._motor = motor 
        
    @property
    def numero_radios(self) -> int:
        return self._numero_radios
        
    @numero_radios.setter
    def numero_radios(self, numero_radios: int) -> None:
        self._numero_radios = numero_radios
        
    @property
    def cuadro(self) -> str:
        return self._cuadro
        
    @cuadro.setter
    def cuadro(self, cuadro: str) -> None:
        self._cuadro = cuadro
        
    @property
    def motor(self) -> str:
        return self._motor
        
    @motor.setter
    def motor(self, motor: str) -> None:
        self._motor = motor        
        
    def __str__(self) -> str:
        return (f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, "
                f"Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.numero_radios}")