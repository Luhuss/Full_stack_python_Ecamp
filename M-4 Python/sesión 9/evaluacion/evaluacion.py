import os

def get_path(directorio, nombre_archivo):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(root_dir, directorio)
    file_path = os.path.join(folder_path, nombre_archivo)
    return file_path

def crear_directorio(directorio):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(root_dir, directorio)
    os.makedirs(folder_path, exist_ok=True)

def crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'x') as file:
            file.write('')
    except FileExistsError:
        print('Error: archivo ya existe')

def escribir_archivo(lista, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            for i in lista:
                file.write(i + '\n')
    except FileNotFoundError:
        print('Error: Archivo no existe')

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            datos = file.readlines()
            return datos
    except FileNotFoundError:
        print('Error: Archivo no existe')
        return []  # Devuelve una lista vacía en caso de error

def agregar_datos(lista, nombre_archivo):
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as file:
            for i in lista:
                file.write(i + '\n')
    except FileNotFoundError:
        print('Error: Archivo no existe')

def cambiar_palabra(palabra_existente, palabra_nueva, lista):
    lista_nueva = []
    contador_palabras = 0
    for i in lista:
        if palabra_existente in i:
            nueva_linea = i.strip().replace(palabra_existente, palabra_nueva)
            lista_nueva.append(nueva_linea)
            contador_palabras += 1
        else:
            lista_nueva.append(i.strip())
    return lista_nueva, contador_palabras

# Crear directorio y archivo si no existen
crear_directorio('data')
ruta_archivo = get_path('data', 'informacion.dat')
crear_archivo(ruta_archivo)

# Escribir datos iniciales en el archivo
datos_iniciales = [
    "Datos de información en la línea 1",
    "Datos de información en la línea 2",
    "Datos de información en la línea 3",
    "Datos de información en la línea 4",
    "Datos de información en la línea 5",
    "Este en una nueva línea en el archivo",
    "agregando la segunda línea del archivo",
    "finalizando la línea agregada"
]
escribir_archivo(datos_iniciales, ruta_archivo)

# Leer el archivo, cambiar palabras y escribir el resultado
lista_datos = leer_archivo(ruta_archivo)
lista_datos_reemplazados, contador_palabras_reemplazadas = cambiar_palabra('información', 'procesamiento', lista_datos)
escribir_archivo(lista_datos_reemplazados, ruta_archivo)

print(f'Se reemplazaron {contador_palabras_reemplazadas} palabras')

