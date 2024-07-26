let suma = 1 + 2
let resta = 3 - 2
let multiplicacion = 2 * 4
let division = 35 / 5
let modulo = 345 % 8
let exponencial = 123 ** 3

let logicaAnd = suma && resta
let logicaOr = suma || resta
let logicaNot = !suma

let asignacion = suma / resta
let comparacionEq = suma === resta
let comparacionEgt = suma >= resta
let comparacionLgt = suma <= resta
let comparacionLt = suma < resta
let comparacionGt = suma > resta
let comparacionNe = suma !== resta

// IF, IF ELSE, TRY CATCH, TRY CATCH FINALLY, DO, DO WHILE, WHILE, FOR EACH, FOR, FOR OF, TERNARIA

for (let numero = 10; numero <= 55; numero++) {
  if (numero % 2 === 0 && numero !== 16 && numero % 3 !== 0) {
    console.log(numero)
  }
}