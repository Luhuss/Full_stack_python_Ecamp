'''
Custom exception, son exceptiones creadas por el desarrollador y que simplemente heredan de la clase base Exception
'''
import json # Importamos la librería json para poder mostrar los mensajes de error en formato JSON.

class CustomException(Exception):
    # constructor
    def __init__(self, mensaje, codigo) -> None:
        super().__init__(mensaje)
        self.codigo = codigo
        
        
def excepcion_propia():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            raise CustomException("Ha sucedido un error de negocio", 460) # ejecutar una excepcion personalizada
    except ValueError as e:
        # print("Error, ingrese un numero")
        print(json.dumps({'mensaje': 'Error: ingrese un número'}))
    except CustomException as e:
        # print(f'Mensaje: {e}')
        # print(f'Codigo: {e.codigo}')
        response = {
            'mensaje': str(e),
            'codigo' : e.codigo
        }
        print(json.dumps(response))
    
    

excepcion_propia()

# {
#     'mensaje': 'Ha sucedido un error de negocio',
#     'codigo' : 460
# }


# import json  # Importamos la librería json para poder mostrar los mensajes de error en formato JSON.

# Definición de una excepción personalizada que hereda de la clase base Exception.
# class CustomException(Exception):
    # Constructor de la excepción personalizada
#    def __init__(self, mensaje, codigo) -> None:
#        super().__init__(mensaje)  # Llama al constructor de la clase base Exception, pasándole el mensaje de error.
#        self.codigo = codigo  # Se guarda el código de error personalizado.

# Función que ejecuta un ejemplo con manejo de excepciones
#def excepcion_propia():
#    try:
        # Se solicita al usuario que ingrese su edad, y se convierte el valor ingresado a un número entero.
#        edad = int(input("Ingrese su edad: "))

        # Si la edad es menor que 0, se lanza una excepción personalizada.
#        if edad < 0:
#            raise CustomException("Ha sucedido un error de negocio", 460)  # Se lanza la excepción personalizada con un mensaje y un código de error.

    # Si el usuario ingresa algo que no es un número, se captura la excepción ValueError.
#    except ValueError as e:
        # En lugar de mostrar el error directamente, se imprime un mensaje en formato JSON.
#        print(json.dumps({'mensaje': 'Error: ingrese un número'}))

    # Si la excepción lanzada es de tipo CustomException (por ejemplo, cuando la edad es negativa).
#    except CustomException as e:
        # Se crea un diccionario con el mensaje y el código de la excepción personalizada.
#        response = {
#            'mensaje': str(e),  # Se convierte el mensaje de la excepción a una cadena de texto.
#            'codigo' : e.codigo  # Se accede al código de error de la excepción.
#       }
        # Se imprime el diccionario en formato JSON para simular una respuesta de error más estructurada.
#        print(json.dumps(response))

# Llamada a la función que ejecuta el proceso.
#excepcion_propia()

# Ejemplo de salida si la edad ingresada es negativa:
# {
#     'mensaje': 'Ha sucedido un error de negocio',
#     'codigo' : 460
# }


#Resumen de los comentarios:
#CustomException es una clase de excepción personalizada que acepta un mensaje y un código de error.
#En la función excepcion_propia, se capturan dos tipos de excepciones:
#ValueError: Ocurre cuando el usuario ingresa algo que no es un número.
#CustomException: Se lanza cuando la edad ingresada es negativa.
#La salida se muestra en formato JSON, lo que facilita el manejo de errores en aplicaciones que puedan necesitar respuestas en este formato estructurado.
