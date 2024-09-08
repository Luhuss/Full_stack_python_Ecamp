class Banco:
    def __init__(self, nombre, codigo_banco, direccion):
        self.nombre = nombre
        self.codigo_banco = codigo_banco
        self.direccion = direccion
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
class Cliente:
    def __init__(self, nombre, direccion, numero_id):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_id = numero_id
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo, cliente, estado_cuenta=True):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.numero_id_cliente = cliente.numero_id
        self.estado_cuenta = estado_cuenta
        
    def deposito(self, monto):
        self.saldo += monto
        print(f'Depositado: {monto}, Nuevo saldo: {self.saldo}')
        
    def retiro(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f'Retirado: {monto}, Nuevo saldo: {self.saldo}')
        else:
            print(f'Saldo insuficiente. Saldo actual: {self.saldo}')
            
    def consulta_saldo(self):
        print(f'Saldo actual: {self.saldo}')
        
class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, titular, saldo, cliente, numero_retiros=0):
        super().__init__(numero_cuenta, titular, saldo, cliente)
        self.numero_retiros = numero_retiros
        
    def retiro(self, monto):
        super().retiro(monto)
        self.numero_retiros += 1
        print(f'Retiros realizados: {self.numero_retiros}')
        
class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, titular, saldo, cliente, saldo_rojo=0):
        super().__init__(numero_cuenta, titular, saldo, cliente)
        self.saldo_rojo = saldo_rojo
        
    def retiro(self, monto):
        if monto <= self.saldo + self.saldo_rojo:
            self.saldo -= monto
            if self.saldo < 0:
                print(f'Saldo en rojo: {self.saldo}')
            else:
                print(f'Retirado: {monto}, Nuevo saldo: {self.saldo}')
        else:
            print(f'Limite de sobregiro alcanzado. Saldo actual: {self.saldo}, Limite: {self.saldo_rojo}')
            

# Ejemplo de uso

# Crear banco
banco = Banco("Banco central", "BC001", "Calle Principal 123")

# Crear cliente
cliente1 = Cliente("Juan Perez", "Avenida Siempre Viva 742", "123456789")

# Crear cuentas
cuenta_ahorro = CuentaAhorro("0001", "Juan Perez", 1000, cliente1)
Cuenta_corriente = CuentaCorriente("0002", "Juan Perez", 500, cliente1, 300)

# Asignar cuentas al cliente
cliente1.agregar_cuenta(cuenta_ahorro)
cliente1.agregar_cuenta(Cuenta_corriente)

# Agregar cuentas al banco
banco.agregar_cuenta(cuenta_ahorro)
banco.agregar_cuenta(Cuenta_corriente)

# Operaciones
cuenta_ahorro.deposito(200)
cuenta_ahorro.retiro(150)
cuenta_ahorro.consulta_saldo()

Cuenta_corriente.deposito(100)
Cuenta_corriente.retiro(700)
Cuenta_corriente.consulta_saldo()

'''
Explicación del código:
Clase Banco:

Esta clase maneja la información del banco y las cuentas asociadas al mismo.
Clase Cliente:

Esta clase guarda la información del cliente y las cuentas que posee.
Clase Cuenta:

Es la clase base que incluye los atributos y métodos comunes a todas las cuentas, como numero_cuenta, saldo, deposito, retiro y consulta_saldo.
Clase CuentaAhorro:

Hereda de Cuenta y agrega un atributo numero_retiros para llevar el control de los retiros realizados.
Clase CuentaCorriente:

También hereda de Cuenta y añade un atributo saldo_rojo para manejar el límite de sobregiro permitido.
Ejemplo de uso:
El ejemplo crea un banco, un cliente, y le asigna dos cuentas (una de ahorro y otra corriente). Luego se realizan varias operaciones como depósitos y retiros, mostrando cómo se comportan las diferentes cuentas según sus reglas.
Este código es una implementación básica del diagrama de clases que compartiste, y debería servir como un buen punto de partida para un sistema bancario más complejo.
'''