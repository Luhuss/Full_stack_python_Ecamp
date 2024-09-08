function Cliente(nombre, rut, clave, saldo) {
    this.nombre = nombre;
    this.rut = rut;
    this.clave = clave;
    this.saldo = saldo;
}

var Cliente1 = new Cliente("Fulanito Perez", "270000001", "0000", 100000);
var Cliente2 = new Cliente("Maria Delgado", "270000002", "0001", 200000);
var Cliente3 = new Cliente("Jose Feliciano", "270000003", "0002", 300000);

var listaClientes = [Cliente1, Cliente2, Cliente3];

var usuario;

document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    var identificador = document.getElementById("identificador").value;
    var password = document.getElementById("password").value;

    for (const iterator of listaClientes) {
        if (iterator.rut === identificador && iterator.clave === password) {
            usuario = iterator;
            break;
        }
    }

    if (usuario) {
        document.getElementById("welcome-message").textContent = "Bienvenido " + usuario.nombre;
        document.getElementById("login-container").style.display = "none";
        document.getElementById("menu-container").style.display = "block";
    } else {
        alert("Datos incorrectos");
    }
});

function verSaldo() {
    document.getElementById("output").textContent = "Su saldo es: " + usuario.saldo;
}

function giro() {
    var retiro = parseInt(prompt("Su saldo actual es: " + usuario.saldo + " Ingrese el monto que desea girar:"));
    if (retiro > usuario.saldo) {
        alert("Saldo insuficiente");
    } else {
        usuario.saldo -= retiro;
        document.getElementById("output").textContent = "Retiro completado, su nuevo saldo es: " + usuario.saldo;
    }
}

function deposito() {
    var deposito = parseInt(prompt("Su saldo actual es: " + usuario.saldo + " Ingrese el monto que desea depositar:"));
    usuario.saldo += deposito;
    document.getElementById("output").textContent = "Deposito completado, su nuevo saldo es: " + usuario.saldo;
}

function salir() {
    alert("Hasta luego!");
    document.getElementById("menu-container").style.display = "none";
    document.getElementById("login-container").style.display = "block";
    document.getElementById("output").textContent = "";
}
