from multipledispatch import dispatch

class Animal:
    
    # Constructor que maneja todos los casos
    def __init__(self, nombre=None, raza=None, edad=None, peso=None):
        self.nombre = nombre
        self.raza   = raza
        self.edad   = edad
        self.peso   = peso
        
    def comer(self):
        print('Comiendo')
        
    def caminar(self):
        print('Caminando')
        
    def dormir(self):
        print('Durmiendo')
        
    def __str__(self) -> str:
        return f'Animal(Nombre:{self.nombre}, Raza:{self.raza}, Edad:{self.edad}, Peso:{self.peso})'
    
# Instancia con constructor con parámetros
perro = Animal('Pepito', 'Dálmata', 1, 6)
gato  = Animal('Kitty', 'Persa', 2, 3)

print(perro)
print(gato)
