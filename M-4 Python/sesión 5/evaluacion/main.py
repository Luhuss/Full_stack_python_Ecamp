# importamos las clases necesarias desde los módulos correspondientes
from trabajador import Trabajador
from persona import Persona
from departamento import Departamento

# Función principal donde se ejecuta el código
if __name__ == "__main__":
    # Creamos el objeto de la clase Trabajador, pasándole los parámetros necesarios
    trabajador = Trabajador("Juan", "Pérez", 2005, "Ingenieria Softwarte", "IS", 20000)
    
    # Imprimimos el diccionario interno del objeto "trabajador", que muestra sus atributos 
    print(trabajador.__dict__)
    # Verificamos si 'trabajador' es una instancia de la clase Persona
    print(f"El objeto es instancia de Persona? {isinstance(trabajador, Persona)}")
    # Verificamos si 'trabajador' es una instancia de la clase Trabajador
    print(f"El objeto es instancia de Trabajador? {isinstance(trabajador, Trabajador)}")
    # Verificamos si 'trabajador' es una instancia de la clase Departamento
    print(f"El objeto es instancia de Departamento? {isinstance(trabajador, Departamento)}")