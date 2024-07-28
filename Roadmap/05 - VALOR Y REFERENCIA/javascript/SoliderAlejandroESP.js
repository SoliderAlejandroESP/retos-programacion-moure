// Por valor (integer, float, string, char)
let valor1 = 10
let valor2 = valor1

console.log(valor1)
console.log(valor2)

valor1 = 20

console.log(valor1)
console.log(valor2)

// Por referencia (objetos: oid -> contenido)
let array1 = [1, 2, 3] // oid: 4
let array2 = array1 // oid array2 = oid array1

console.log(array1)
console.log(array2)

array1.push(4)

console.log(array1)
console.log(array2)

// Funcion por valor
function sumaValor(num1, num2) {
  num1 = 20
  num2 = 30
  return num1 + num2
}

let num1 = 10
let num2 = 20

console.log(num1)
console.log(num2)
console.log(sumaValor(num1, num2))
console.log(num1)
console.log(num2)

// Funcion por referencia
function sumaReferencia(arrayNums) {
  arrayNums[0] = arrayNums[0] * 2
  arrayNums[1] = arrayNums[1] / 2
  return arrayNums[0] + arrayNums[1]
}

let arrayNums = [2, 4]

console.log(arrayNums)
console.log(sumaReferencia(arrayNums))
console.log(arrayNums)

console.log('----------------------------')

// 
// 
// 
// Su retorno se asignan a dos variables distintas de las originales
// Imprimir por pantalla el valor primero, antiguo y nuevo de las variables
let unoArg1 = 10
let unoArg2 = 20

function programaUno(arg1, arg2) {
  let aux = arg1
  arg1 = arg2
  arg2 = aux
  return [arg1, arg2]
}

let returnUno = programaUno(unoArg1, unoArg2)
let newUnoArg1 = returnUno[0]
let newUnoArg2 = returnUno[1]

console.log(unoArg1)
console.log(unoArg2)
console.log(newUnoArg1)
console.log(newUnoArg2)


let dosArray1 = [1, 2, 3] // oid: 1
let dosArray2 = [4, 5, 6] // oid: 2

function programaDos(arg1, arg2) {
  console.log(arg1, arg2)
  let aux = arg1
  arg1 = arg2
  arg2 = aux
  console.log(arg1, arg2)
  return [arg1, arg2]
}

let returnDos = programaDos(dosArray1, dosArray2)
let newDosArray1 = returnDos[0]
let newDosArray2 = returnDos[1]

console.log(dosArray1)
console.log(dosArray2)
console.log(newDosArray1)
console.log(newDosArray2)