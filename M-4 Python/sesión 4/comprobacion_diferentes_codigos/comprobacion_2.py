# Clase Libro que usa un diccionario en lugar de atributos individuales
class Libro:
    def __init__(self):
        self.atributos = {}

# Crear las instancias de la clase Libro
libro_1 = Libro()
libro_1.atributos['autor'] = 'Dan Brown'
libro_1.atributos['titulo'] = 'Infierno'

libro_2 = Libro()
libro_2.atributos['autor'] = 'Dan Brown'
libro_2.atributos['titulo'] = 'El Código Da Vinci'
libro_2.atributos['ann_de_publicacion'] = 2003

# Imprimir el diccionario de atributos de cada libro
print("Atributos de libro_1:", libro_1.atributos)
print("Atributos de libro_2:", libro_2.atributos)
