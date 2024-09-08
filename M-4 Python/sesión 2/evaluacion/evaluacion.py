'''
Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad,
estatura y peso. 
'''

class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
        
    def get(self, atributo):
        return getattr(self, atributo)
    
    def set(self, atributo, valor):
        setattr(self, atributo, valor)
    
    def __str__(self) -> str:
        return f'Persona(nombre: {self.nombre}, apellido: {self.apellido}, sexo: {self.sexo}, edad: {self.edad}, estatura: {self.estatura}, peso: {self.peso})'
    
# Crear instancias de la clase Persona
Persona_1 = Persona('Pedro', 'Vivas', 'Masculino', 20, 1.78, 68)
Persona_2 = Persona('Juan', 'Camargo', 'Masculino', 18, 1.8, 75)

# Modificar los atributos solicitados usando set
Persona_1.set('edad', 21)
Persona_2.set('apellido', "Santiago")

# Mostras actualización 
print("Actualizaciones de Persona_1 y Persona_2:")
print(Persona_1)
print(Persona_2)