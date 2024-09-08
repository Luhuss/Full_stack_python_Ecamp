# Clase Libro con método __setattr__ redefinido
class Libro:
    def __setattr__(self, nombre, valor):
        self.__dict__[nombre] = valor

# Crear las instancias de la clase Libro
libro_1 = Libro()
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'

libro_2 = Libro()
libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Da Vinci'
libro_2.ann_de_publicacion = 2003

# Imprimir el valor del atributo __dict__ de cada libro
print("Atributos de libro_1:", libro_1.__dict__)
print("Atributos de libro_2:", libro_2.__dict__)
