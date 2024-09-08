# Definimos la clase libro
class Libro:
    pass

# Cremos las intancias de la clase libro
libro_1 = Libro()
libro_2 = Libro()

# Se asignan atributos a cada objeto
libro_1.autor = 'Dan Brown'
libro_2.titulo = 'Infierno'

libro_1.autor = 'Dan Brown'
libro_2.titulo = 'EL Código Da Vinci'
libro_2.ann_de_publicacion = 2003

# Imprimir el valor del atributo __dict__ de cada libro
print("Atributos de lobro_1:", libro_1.__dict__)
print("Atributos de libro_2:", libro_2.__dict__)
