'''
Debe crear dos instancias u objetos de la clase Animal, cuyos objetos son un caballo y un león, con
las siguientes características particulares:
'''


class Animal:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        
    def __str__(self) -> str:
        return f'Animal(nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}, peso: {self.peso})'
        
# Crear instancias de la clase Animal
caballo = Animal('Zeus', 5, 'Pura sangre', 450)
leon = Animal('Boulder', 10, 'Atlas', 130)

# Imprimir la información de cada objeto
print(caballo)
print(leon)


# Explicación:
# Método __str__: Este método ahora retorna una cadena que describe al animal con sus atributos (nombre, edad, #raza, peso).

# Nombres de variables: Cambié León a leon para mantener la consistencia en el estilo de nombres de variables en # Python, donde se recomienda usar minúsculas para nombres de variables.
