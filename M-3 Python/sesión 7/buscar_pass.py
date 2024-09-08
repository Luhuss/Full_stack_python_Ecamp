def verificar_contraseña():
    contraseña_correcta = "1234"  # Contraseña predefinida
    contraseña_ingresada = ""

    while contraseña_ingresada != contraseña_correcta:
        contraseña_ingresada = input("Ingresa la contraseña: ")
        if contraseña_ingresada == contraseña_correcta:
            print("¡Contraseña correcta!")
        else:
            print("Contraseña incorrecta, intenta nuevamente.")

verificar_contraseña()


'''
Explicación:
contraseña_correcta: Es la contraseña que el usuario debe ingresar correctamente para salir del bucle.
while contraseña_ingresada != contraseña_correcta: Mantiene el bucle activo hasta que la contraseña ingresada coincida con la predefinida.
input("Ingresa la contraseña: "): Solicita al usuario que ingrese la contraseña.
if contraseña_ingresada == contraseña_correcta:: Verifica si la contraseña ingresada es correcta y, si lo es, imprime un mensaje de confirmación; de lo contrario, solicita al usuario intentarlo nuevamente.
'''