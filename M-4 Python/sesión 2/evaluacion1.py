'''
Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad,
estatura y peso. 
'''

class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get(self, atributo):
        return getattr(self, atributo)

    def set(self, atributo, valor):
        setattr(self, atributo, valor)

    def __str__(self) -> str:
        return (f'Persona(nombre: {self.nombre}, apellidos: {self.apellidos}, sexo: {self.sexo}, '
                f'edad: {self.edad}, estatura: {self.estatura}, peso: {self.peso})')

# Crear las dos instancias de Persona con los datos proporcionados
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

# Modificar los atributos solicitados usando set
persona_1.set('edad', 21)
persona_2.set('apellidos', "Santiago")

# Mostrar por pantalla las actualizaciones respectivas
print("Actualizaciones de Persona_1 y Persona_2:")
print(persona_1)
print(persona_2)


# Explicación:
# Métodos get y set genéricos:

# get(self, atributo): Este método toma el nombre del atributo como una cadena y devuelve su valor usando getattr.
# set(self, atributo, valor): Este método toma el nombre del atributo como una cadena y asigna un nuevo valor usando setattr.
# Uso dinámico de getattr y setattr:

# getattr(objeto, "atributo"): Devuelve el valor de atributo del objeto.
# setattr(objeto, "atributo", valor): Asigna valor al atributo del objeto.
# Reducción de código:

# Este enfoque evita tener que escribir un método get y set para cada atributo, haciendo que el código sea más compacto y flexible.
