# Clase Libro definida
class Libro:
    pass

# Crear las instancias de la clase Libro
libro_1 = Libro()
libro_2 = Libro()

# Usar setattr para asignar atributos dinámicamente
setattr(libro_1, 'autor', 'Dan Brown')
setattr(libro_1, 'titulo', 'Infierno')

setattr(libro_2, 'autor', 'Dan Brown')
setattr(libro_2, 'titulo', 'El Código Da Vinci')
setattr(libro_2, 'ann_de_publicacion', 2003)

# Imprimir el valor del atributo __dict__ de cada libro
print("Atributos de libro_1:", libro_1.__dict__)
print("Atributos de libro_2:", libro_2.__dict__)
