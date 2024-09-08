c = 'hola un mensaje' # variable global


def imprimir_mensaje():
    c = 'cambio de valor' # variable local
    print(c)
    
def imprimir_mensaje_c(c):
    c = 'cambio de valor'
    print(c)
    
def imprimir_mensaje_c_e(c, e):
    c = 'cambio de valor'
    print(c)  
    
def imprimir_mensaje_otra(c):
    a = c
    print(a)        
    
imprimir_mensaje()            
