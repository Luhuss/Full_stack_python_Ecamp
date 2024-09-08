// ciclos en javascript, ciclo for (para), while(mientras), do while 

// ciclo for
//for (let index = 0; index < array.length; index++) {
//    const element = array[index];
//}

for (let i = 0; i < 5; i++) {
    console.log(i)
}

// ciclo while, solo se ejecuta si la condición se cumple
//while (condition) {
//    
//}

let = 0;
while (i < 5) {
    console.log(i);
    i++; // i += 1 (para aumentar el valor de 1 en 1 se puede hacer de estas dos formas)
}

// do while, se ejecuta al menos una vez
i = 0;
do {
    console.log(i);
    i++; // aumentar el valor del iterador para salir del ciclo
} while (i < 5);

//////////////////////////////////////////////////////////////////////////////////////////
let colores = ["verde", "rojo", "azul"] //[0,1,2,]
                                        // ["verde", "rojo", "azul"] el 0 representa al color verde, el 1 al rojo y el 2 al azul

// con ciclo for
for (let i = 0; i < colores.length; i++) {
    console.log(colores[i]);
    
}

// ciclo while
i = 0;
while (i < colores.length) {
    console.log(colores[i]);
    i++;
}

// ciclo do while
i = 0;
do {
    console.log(colores[i]);
    i++;
} while (i < colores.length);

let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
i = 0;
for (let i = 0; i < numeros.length; i++) {
    console.log (numeros[i]);
    
}

let amigos = ["Carlos", "Alan", "Cony", "Pamela"];

for (let i = 0; i < amigos.length; i++) {
    console.log (amigos[i]);
    
}

i = 10;
while (i > 0) {
    console.log(i);
    i--;
    
}

let numero;

do {
    numero = prompt("Ingrese un número:")

    numero = parseInt(numero);

} while (numero <= 100 && !isNaN(numero));

console.log("Número mayor a 100 ingresado");