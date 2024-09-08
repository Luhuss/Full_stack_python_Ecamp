'''
Los objetos seran tratados como simples objetos y no por su tipo

Lo que diferencia un objeto de otro son sus atributos y funciones

'''


class Perro:
    def hablar(self):
        print('guau')
        
    def sentarse(self):
        print('sentado')
    
class Gato:
    def hablar(self):
        print('miau')
    
class Pato:
    def hablar(self):
        print('cuac')
        
def llamar_hablar(objeto):
    objeto.hablar()
    
def recorrer_lista_objetos(lista):
    for objeto in lista:
        objeto.hablar()
        if isinstance(objeto, Perro): # verificar si el objeto es un perro , verificación de tipo
            objeto.sentarse()

perro = Perro()
gato = Gato()
pato = Pato()
    
llamar_hablar(perro)
llamar_hablar(gato)
llamar_hablar(pato)

recorrer_lista_objetos([perro, gato, pato])

'''
Definición de Clases:
Clase Perro:

Tiene dos métodos:
hablar(): Imprime "guau".
sentarse(): Imprime "sentado".
Clase Gato:

Tiene un método:
hablar(): Imprime "miau".
Clase Pato:

Tiene un método:
hablar(): Imprime "cuac".
Definición de Funciones:
Función llamar_hablar(objeto):

Toma un objeto como argumento y llama a su método hablar().
Función recorrer_lista_objetos(lista):

Toma una lista de objetos como argumento.
Recorre la lista y, para cada objeto en la lista, llama a su método hablar().
Verifica si el objeto es una instancia de la clase Perro utilizando isinstance(objeto, Perro). Si es un Perro, llama al método sentarse().
Ejecución del Código:
llamar_hablar(perro):

Llama al método hablar() del objeto perro, que imprime "guau".
llamar_hablar(gato):

Llama al método hablar() del objeto gato, que imprime "miau".
llamar_hablar(pato):

Llama al método hablar() del objeto pato, que imprime "cuac".
recorrer_lista_objetos([perro, gato, pato]):

Recorre la lista [perro, gato, pato] y ejecuta los métodos hablar() de cada objeto.
Para perro, imprime "guau" y luego "sentado" porque el objeto es una instancia de Perro.
Para gato, imprime "miau".
Para pato, imprime "cuac".
'''

#Conceptos Clave:
#Polimorfismo: Se refiere a la capacidad de diferentes clases para implementar el mismo método de formas diferentes. Aquí, Perro, Gato, y Pato tienen un método hablar() con implementaciones diferentes.
#Verificación de tipo (isinstance): Se utiliza para verificar si un objeto es una instancia de una clase específica. En este caso, se usa para verificar si un objeto es un Perro para luego llamar al método sentarse().
#Este código es un buen ejemplo de cómo se puede aplicar el polimorfismo y la verificación de tipos en Python.
