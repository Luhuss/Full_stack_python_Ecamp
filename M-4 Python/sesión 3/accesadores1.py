class Accesadores:
    def __init__(self):
        self.atributo_publico = 'public'  # Atributo público
        self._atributo_privado = 'private'  # Atributo "protegido", accesible en subclases o mediante métodos get/set
        self.__atributo_protegido = 'protected'  # Atributo "privado", accesible solo dentro de la clase
    
    def get_variable_privada(self):  # Método para acceder a un atributo "privado"
        return self._atributo_privado
    
    def set_variable_privada(self, valor):  # Método para modificar un atributo "privado"
        self._atributo_privado = valor 


# Crear una instancia de Accesadores
objeto = Accesadores()

# Acceso a un atributo "privado" utilizando name mangling
print(objeto._Accesadores__atributo_protegido)  # Salida: 'protected'

# Acceso a un atributo "protegido" mediante un método público
print(objeto.get_variable_privada())  # Salida: 'private'

# Acceso a un atributo público directamente
print(objeto.atributo_publico)  # Salida: 'public'

# Intentar acceder directamente a un atributo "privado" (esto dará un error)
print(objeto.__atributo_protegido)  # Esto lanzará un AttributeError

#Puntos clave:
#Atributos Públicos: atributo_publico es accesible desde cualquier parte del código.
#Atributos "Protegidos": _atributo_privado es accesible desde fuera de la clase, pero por convención, se considera que debería ser tratado como protegido.
#Atributos "Privados": __atributo_protegido se renombra internamente para evitar accesos accidentales o no deseados. Se puede acceder usando objeto._Accesadores__atributo_protegido, pero esto se considera mala práctica en la mayoría de los casos.