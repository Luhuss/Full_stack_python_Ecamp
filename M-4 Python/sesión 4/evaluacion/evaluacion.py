# Clase padre Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    def movimiento(self):
        return f'{self.nombre} se está movimiendo.'

# Subclase Maratonista, que hereda de Persona
class Maratonista(Persona):
    def movimiento(self):
        return f'{self.nombre} está trotando.'

# Subclase Ciclista, que hereda de Persona
class Ciclista(Persona):
    def movimiento(self):
        return f'{self.nombre} está rodando.'

# Se crean instancias de cada clase
persona         = Persona("Pepé")
maratonista     = Maratonista("Ursula")
ciclista        = Ciclista("León")

# Se imprime los movimientos de cada uno
print(persona.movimiento())
print(maratonista.movimiento())
print(ciclista.movimiento())

# Explicación:
# Clase base Persona: Esta clase tiene un atributo nombre y un método movimiento que retorna que la persona está caminando.
# Subclase Maratonista: Esta clase hereda de Persona y sobreescribe el método movimiento para indicar que está trotando.
# Subclase Ciclista: Esta clase también hereda de Persona y sobreescribe el método movimiento para indicar que está rodando.