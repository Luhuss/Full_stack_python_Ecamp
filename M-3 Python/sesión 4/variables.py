# las variables de declaran con un nombre, que es su identificador
#van escritas en snake_case
#identificador = valor
nombre_variable = 'una variable'
nombre_variable = 2 #sustituye el valor de la variable

print(nombre_variable) #2

# variables locales y variables globales
s = 'una variable global'

#las variables locales existen dentro de los bloques de codigo
# funciones, condicionales (if, else if), bucles (ciclos)
def f(cualquier_nombre):
    cualquier_nombre = 'sustituimos la variable global'
    variable_local = 'una variable local'
    print(s)
    
f(s) #invocando funcion f
#print(variable_local) #error, variable local no definida
print(s) #una variable global

# s = "esta es una variable global" #variable gloabal
# def f():
#    s = "esta es una variable local" #variable local
#    print(s) #este print se debe hacer para imprimir la variable local
# print(s) # de esta forma se imprime s = "esta es una variable global"
# f() # de esta forma de imprime la variable s = "esta es una variable local"