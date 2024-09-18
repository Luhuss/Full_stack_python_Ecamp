class Vehiculo:
    def __init__(self, marca :str, modelo :str, numero_ruedas :int) -> None:
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas
        
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
        
    def __str__(self) -> str:
        return (f"Datos del automovil: Marca {self._marca}, Modelo {self._modelo} ruedas {self._numero_ruedas}")
        