// Cada uno de los clientes de nuestro bando contará con un nombre.
// un identificador, una clave y un saldo en su cuenta.
// Se debe contar con al menos 3 clientes registrados.

// Los objetos comienzan con la primera letra en mayuscula
// Las variables comienzan con la primera letra en minuscula

// nombre | rut | clave | saldo
function Cliente(nombre, rut, clave, saldo) {
    this.nombre = nombre
    this.rut = rut
    this.clave = clave
    this.saldo = saldo 
}

// declaracion para crear un objeto cliente
var Cliente1 = new Cliente("Fulanito perez", "270000001", "0000", 100000)
var Cliente2 = new Cliente("Maria Delgado", "270000002", "0001", 200000)
var Cliente3 = new Cliente("Jose Feliciano", "270000003", "0002", 300000)
var Cliente4 = new Cliente("Uzumaki Naruto", "270000004", "0003", 100000)
var Cliente5 = new Cliente("Kenshi Himura", "270000005", "0004", 200000)
var Cliente6 = new Cliente("Killua Zoldic", "270000006", "0005", 300000)

var listaClientes = [Cliente1, Cliente2, Cliente3, Cliente4, Cliente5, Cliente6] // lista para recorrer y buscar

// Cuando se ingrese el identificador y la clave,
// se revisará si coincide con alguno de los clientes registrado.
// Si no coincide, se mostrará un mensaje de error.

alert("Bienvenido a Banca en linea")
var identificador = prompt("Ingrese su identificador") // ingreso de valores
var password = prompt("Ingrese su password") // ingreso de valores

// recorrer la lista con clientes
var usuario;
for (const iterator of listaClientes) {
    if (iterator.rut === identificador && iterator.clave === password) {
        usuario = iterator; // cliente existe
        break;
    }
}

// validación si el usuario fue encontrado 
if (usuario) {
    alert("Bienvenido " + usuario.nombre)
    menu(usuario) // llamada a funcion menu cuando el cliente existe
} else {
    alert("Datos incorrectos")
}


// funcion menu
function menu(usuario) { //"Seleccione que desea hacer: 1.- Ver saldo. 2- 3.-"
    do{
        var opcion = prompt("Seleccione que desea hacer:\n"+
        "1.- Ver saldo.\n" +
        "2.- Realizar giro\n" +
        "3.- Realizar deposito\n" +
        "4.- Salir" 
        //"5.- Cambio de clave"
    )

        switch (opcion) {
            case "1": //Ver saldo
                verSaldo(usuario)
                break;
            case "2": //Realizar giro
                giro(usuario)
                break;
            case "3": //Realizar deposito
                deposito(usuario)
                break;    
            case "4": //Salir
                salir(usuario)
                break;    
            //case "5": //Salir
                //cambioClave(usuario)
                //break;    
            default: // Caso que se muestre por default si no cumple ningún caso
                alert("Opción incorrecta")
                break;
        }

    } while (opcion != "6"); 
}

function verSaldo(params) {
    alert("Su saldo es: " + params.saldo)
}

function giro(usuario) {
    var retiro = parseInt(prompt("Su saldo actual es: " + usuario.saldo + " Ingrese el monto que desea girar:"))
            if (retiro > usuario.saldo) {
                alert("Saldo insuficiente")
            } else {
                usuario.saldo -= retiro // acumulación de la resta del retiro al saldo del usuario
                alert("Retiro completado, su nuevo saldo es: " + usuario.saldo)
            }
}

function deposito(usuario) {
    var deposito = parseInt(prompt("Su saldo actual es: " + usuario.saldo + " Ingrese el monto que desea depositar:"))
            usuario.saldo += deposito
            alert("Deposito completado, su nuevo saldo es: " + usuario.saldo)
}

function salir(usuario) {
    alert("Hasta luego!")
}

//function cambioClave(usuario) {
    //var nuevaClave = prompt("Ingrese su nueva clave:")
    //if (nuevaClave) {
        //usuario.clave = nuevaClave;
        //alert("Clave cambiada exitosamente")
    //} else{
        //alert("Cambio de clave cancelado")
    //}
// }