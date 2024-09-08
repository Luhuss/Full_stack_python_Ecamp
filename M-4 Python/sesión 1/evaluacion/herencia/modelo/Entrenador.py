from Persona import Persona

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad) # constructor de super clase
        
        # atributos propios de la clase Entrenador
        self.id_federacion = id_federacion
    
    
    # Métodos heredados    
    #def concentrarse(self):
    #    Persona.concentrarse() # acceso estatico a traves del nombre de la clase
            
    # Métodos heredados
    def concentrarse(self):
        super().concentrarse()
        
    def viajar(self):
        super().viajar()
        
    # métodos propios de la clase Entrenador
    def dirigir_partido(self):
        print("El entrenador dirige el partido")
        
    def dirigir_entrenamiento(self):
        print("El entrenador dirige el entrenamiento")