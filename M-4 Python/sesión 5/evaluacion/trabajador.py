# Importamos las clases necesarias desde los módulos correspondientes
from persona import Persona
from departamento import Departamento

# Definimos la clase Trabajador, que hereda de las clases Persona y Departamento
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, annio, nombre_dpto, nombre_corto_dpto, salario):
        # Llamamos al constructor de la clase Persona con super(), para inicializar los atributos de Persona
        super().__init__(nombre, apellido, annio)
        # Llamamos explícitamente al constructor de Departamento para inicializar sus atributos
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        # Asignamos el salario como un atributo específico de Trabajador
        self.salario = salario
        
    