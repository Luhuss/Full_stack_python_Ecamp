###### version de Python
python3 --version 

###### listar paquetes instalados 
pip list

##### ejecutar instalador de paquetes
pip --version

##### crear un entorno virtual
> abrir carpeta en la terminal donde se quiera generar el entorno virtual
> click derecho sobre el archivo seleccionado -> clickear -> abrir terminal en entorno integrado
> cd.. # para ir a la carpeta anterior
> ls   # verificar que estamos en la carpeta correcta
> pwd  # verificar ruta actual


python3 -m venv env 
python3 -m venv nombre_entorno_virtual 
python3 -m venv proyecto_django

##### ejecutar entorno virtual
nombre_entorno -> bin -> activate.ps1 (para activar)
nombre_entorno -> bin -> activate

##### crear una carpeta para tu proyecto
mkdir mi_proyecto 
proyecto_django

##### Crear el entorno virtual
python3 -m venv nombre_entorno
python3 -m venv proyecto_django

##### activar el entorno virtual
source venv/bin/activate
source proyecto_django/bin/activate

##### si todo está correcto
(venv) nombreusuario@nombre-mac mi_proyecto %
(proyecto_django) luismaraboli@MacBook-Air-de-Luis rebound %

##### instalar dependencias (opcional)
pip install nombre_paquete

##### desactivar el entorno virtual
deactivate

/*
Abrir la Terminal.
Verificar Python 3 con python3 --version.
Crear una carpeta de proyecto: mkdir mi_proyecto && cd mi_proyecto.
Crear el entorno virtual: python3 -m venv venv.
Activar el entorno virtual: source venv/bin/activate.
Desactivar el entorno virtual cuando sea necesario con deactivate.
*/

###### instalar django en el entorno virtual mediante el instalador de paquetes (pip)
pip install django

##### comando de ayuda pip
pip help

##### para guardar las dependencias en un archivo que puedas reutilizar
pip freeze > requirements.txt

##### eliminar el entorno virtual
rm -rf nombre_del_entorno

##### ejecuta el siguiente comando para instalar todas las dependencias listadas en :requirements.txt
pip install -r requirements.txt
