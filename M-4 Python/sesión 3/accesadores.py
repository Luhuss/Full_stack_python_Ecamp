class Accesadores:
    def __init__(self):
        self.atributo_publico = 'public' # atributo accedido en toda la estructura
        self._atributo_privado = 'private' # al iniciar con _ se declara un atributo privado en Python, atributo solo accediso en las subclases o por getters o setter
        self.__atributo_protegido = 'protected' # __ para un atributo protegido, accedido en la case que está declarado
        
    def get_variable_privada(self): # acceso a una variable declarada como private
        return self._atributo_privado
    
    def set_variable_privada(self, valor): # asignacion a una variable declarada como private
        self._atributo_privado = valor 
        
    
objeto = Accesadores()
print(objeto._Accesadores__atributo_protegido) # acceso a un atributo protegido 

print(objeto.get_variable_privada()) # acceso a una variable privada

print(objeto.atributo_publico) # acceso a un atributo protegido

print(objeto.__atributo_protegido) # AttributeError: 'Accesadores' object has no attribute '__atributo_protegido'. Did you mean: '_atributo_privado'?

