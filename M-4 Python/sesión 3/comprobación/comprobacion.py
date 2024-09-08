# Clase base Persona
class Persona:
    def __init__(self, numero_identificacion, nombre, apellido):
        self.numero_identificacion = numero_identificacion
        self.nombre = nombre
        self.apellido = apellido
        
    def obtener_datos(self):
        return f"ID: {self.numero_identificacion}, Nombre: {self.nombre}, Apellido: {self.apellido}"
    
# Clase derivada Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, numero_identificacion, nombre, apellido, codigo_alumno, matricula):
        # Llamamos al constructor de la clase base para inicializar los atributos de Persona
        super().__init__(numero_identificacion, nombre, apellido)
        self.codigo_alumno = codigo_alumno
        self.matricula = matricula
        
    def obtener_datos(self):
        # Sobreescribimos el método para incluir la información adicional del estudiasnte
        datos_persona = super().obtener_datos()
        return f"{datos_persona}, Código Alumno: {self.codigo_alumno}, Matricula: {self.matricula}"
    
# Ejemplo de uso
persona = Persona("12345678", "Juan", "Perez")
print(persona.obtener_datos())

estudiante = Estudiante("87654321", "Ana", "Gomez", "A001", "2023-001")
print(estudiante.obtener_datos())

'''
Explicación del código:
Clase Persona:

Se define un constructor (__init__) que inicializa los atributos numero_identificacion, nombre, y apellido.
El método obtener_datos() retorna una cadena con los datos de la persona.
Clase Estudiante:

Hereda de la clase Persona, utilizando la función super() para llamar al constructor de la clase base y asegurarse de que los atributos heredados se inicialicen correctamente.
Se añaden dos nuevos atributos: codigo_alumno y matricula.
El método obtener_datos() se sobrescribe para incluir los datos adicionales del estudiante, llamando al método obtener_datos() de la clase base para obtener la información de Persona y añadiendo la información específica de Estudiante.
Ejemplo de uso:
Primero, se crea una instancia de Persona y se muestra la información básica.
Luego, se crea una instancia de Estudiante, que hereda de Persona, y se muestra la información tanto de Persona como de Estudiante.
Este código refleja fielmente el diagrama de clases que has proporcionado, mostrando cómo se puede implementar la herencia y la sobrescritura de métodos en Python.
'''
