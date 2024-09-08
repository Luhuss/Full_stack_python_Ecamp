# diccionarios
# clave: valor

persona_uno = {'nombre' : 'Juan', 'apellido': 'Perez', 'telefono': 123456789} 

persona_dos = {
    'nombre' : 'Fulanito',
    'apellido': 'Rojo',
    'telefono': 123456789
    }

persona_tres = {'nombre' : 'Maria', 'apellido': 'Rosalez', 'telefono': 123456789} 

lista_persona = [persona_uno, persona_dos, persona_tres]
print(lista_persona)
lista_persona[0]['nombre'] = 'Juanito' # Modificar un valor


# se puede declarar tambien de esta forma
personas = {
    'persona_uno' : {'nombre' : 'Juan', 'apellido': 'Perez', 'telefono': 123456789},
    'persona_dos' : {
    'nombre' : 'Fulanito',
    'apellido': 'Rojo',
    'telefono': 123456789
    },
    'persona_tres' : {'nombre' : 'Maria', 'apellido': 'Rosalez', 'telefono': 123456789},
    'persona_cuatro' : {
    'nombre' : 'Fulanito',
    'apellido': 'Rojo',
    'telefono': 123456789,
    'direccion' : {
        'calle': 'calle 1',
        'numero': 123,
        'region': 'Metropolitana'
    }
    }
}
# diccionario[clave] [subclave]
print(personas['persona_uno']['nombre'])
print(personas['persona_cuatro']['direccion']['region'])
