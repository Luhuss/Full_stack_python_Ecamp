class Vehiculo:
    def __init__(self, marca: str, modelo: str, numero_ruedas: int) -> None:
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas
        
    @property
    def marca(self) -> str:
        return self._marca
    
    @marca.setter
    def marca(self, marca: str) -> None:
        self._marca = marca
        
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self._modelo = modelo
        
    @property
    def numero_ruedas(self) -> int:
        return self._numero_ruedas
    
    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas: int) -> None:
        self._numero_ruedas = numero_ruedas
        
    def __str__(self) -> str:
        return (f"Marca {self._marca}, Modelo {self._modelo}, Numero_ruedas {self._numero_ruedas}")
    
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
    def cilindrada(self, cilindrada: int) -> None:
        self._cilindrada = cilindrada
        
    def __str__(self) -> str:
        return (f"Marca {self._marca}, Modelo {self._modelo}, Numero_ruedas {self._numero_ruedas}, Velocidad {self._velocidad} km/h, Cilindrada {self._cilindrada} cc")
    