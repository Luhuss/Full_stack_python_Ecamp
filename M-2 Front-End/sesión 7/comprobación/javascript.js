// solicitar el ingreso de dos numeros y 
// calcular cual es mayor o si tienen el mismo valor.
// en cualquier caso, debes mostrar un mensaje
// indicando cual de los numeros es mayor,
// por ejemplo, si ingresamos 5 y 8



// solicitar el ingreso de dos numeros
var numeroUno = parseInt(prompt("Ingrese el primer número"));
var numeroDos = parseInt(prompt("Ingrese el segundo número"));

// calcular cual es mayor o si tienen el mismo valor
if (numeroUno > numeroDos) {
    // funcion alert(), para ejecutar una ventana emergente con un mensaje o valor
    alert("El primero número es mayor al segundo número ")
} else if(numeroUno == numeroDos){
    alert("Son iguales")
} else {
    alert("El segundo numero es mayor que el primer numero ingresado")
}

