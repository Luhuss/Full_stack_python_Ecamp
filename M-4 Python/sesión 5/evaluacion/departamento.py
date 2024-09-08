# Definimos la clase Departamento
class Departamento:
    """
    Inicializamos una nueva instancia de la clase Departamento.
    
    Args: 
        nombre_dpto (str): El nombre completo del departamento.
        nombre_corto_dpto (str): La abreviatura o nombre corto del departamento
    """
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        # """la funcion deberia ir arriba de la explicación "" pero acusa un error por eso dejo este comentario """
        # Atributo que guarda el nombre completo del departamento
        self.nombre_dpto = nombre_dpto
        # Atributo que guarda el nombre corto o abreviatura del departamento
        self.nombre_corto_dpto = nombre_corto_dpto