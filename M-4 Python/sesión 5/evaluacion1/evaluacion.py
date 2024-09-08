class Persona:
    def __init__(self, nombre, apellido, annio):
        self.nombre = nombre
        self.apellido = apellido
        self.annio = annio
        
class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto
        
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, annio, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellido, annio)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario
        
    def __str__(self) -> str:
        return (f"Trabajador: {self.nombre} {self.apellido} {self.annio} {self.nombre_dpto} {self.nombre_corto_dpto} {self.salario}")
        
trabajador = Trabajador("Juan", "Pérez", 2005, "Ingeniería de softWare", "IS", 20000)

print(trabajador.__dict__)