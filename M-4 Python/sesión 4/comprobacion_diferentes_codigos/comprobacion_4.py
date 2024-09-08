from collections import namedtuple

# Crear una clase inmutable de tipo namedtuple
Libro = namedtuple('Libro', ['autor', 'titulo', 'ann_de_publicacion'])

# Crear las instancias de la clase Libro
libro_1 = Libro(autor='Dan Brown', titulo='Infierno', ann_de_publicacion=None)
libro_2 = Libro(autor='Dan Brown', titulo='El Código Da Vinci', ann_de_publicacion=2003)

# Imprimir los atributos de las instancias (no hay __dict__ en namedtuple, pero podemos mostrar los valores)
print("Atributos de libro_1:", libro_1._asdict())
print("Atributos de libro_2:", libro_2._asdict())
