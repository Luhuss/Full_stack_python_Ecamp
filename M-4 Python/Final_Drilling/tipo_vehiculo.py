import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Final_Drilling.vehiculo import Automovil
from Final_Drilling.vehiculo import Vehiculo

class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: int, cilindrada: int, numero_asiento: int) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._numero_asientos = numero_asiento
        
    @property
    def numero_asientos(self) -> int:
        return self._numero_asientos
    
    @numero_asientos.setter
    def numero_asientos(self, numero_asiento: int) -> None:
        self._numero_asientos = numero_asiento
        
    def __str__(self) -> str:
        return (f"Marca {self._marca}, Modelo {self._modelo}, Numero_ruedas {self._numero_ruedas}, Velocidad {self._velocidad} km/h, Cilindrada {self._cilindrada} cc, Numero_Asientos {self._numero_asientos}")
    
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
        return (f"Marca {self._marca}, Modelo {self._modelo}, Numero_ruedas {self._numero_ruedas}, Velocidad {self._velocidad} km/h, Cilindrada {self._cilindrada} cc, Carga_Maxima {self._carga_maxima} kg.")

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
        return (f"Marca {self._marca}, Modelo {self._modelo}, Numero_ruedas {self._numero_ruedas}, Tipo {self._tipo}")
        
class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo: str, numero_radio: int, cuadro: str, motor: str) -> None:
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self._numero_radio = numero_radio
        self._cuadro = cuadro
        self._motor = motor
        
    @property
    def numero_radio(self) -> int:
        return self._numero_radio
    
    @numero_radio.setter
    def numero_radio(self, numero_radio: int) -> None:
        self._numero_radio = numero_radio
        
    @property
    def cuadro(self) -> int:
        return self._cuadro
    
    @cuadro.setter
    def cuadro(self, cuadro: int) -> None:
        self._cuadro = cuadro
        
    @property
    def motor(self) -> int:
        return self._motor
    
    @motor.setter
    def motor(self, motor: int) -> None:
        self._motor = motor
        
    def __str__(self) -> str:
        return (f"Marca {self._marca}, Modelo {self._modelo}, Numero_ruedas {self._numero_ruedas}, Tipo {self._tipo}, Numero_radio {self._numero_radio}, Cuadro {self._cuadro}, Motor {self._motor}")