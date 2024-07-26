function imprimirHelloWorld() {
  console.log("Hello World!")
}

imprimirHelloWorld()

function retornarNombreUsuario() {
  return "Perico"
}

console.log(retornarNombreUsuario())

function escribirNombreConParametros(nombre) {
  console.log(`Hola, ${nombre}!`)
}

escribirNombreConParametros()

function devolverEstructuraSaludoNombreConParametro(nombre) {
  return `Hola, ${nombre}`
}

console.log(devolverEstructuraSaludoNombreConParametro())

function funcionDentroDeFuncion() {
  function holaMundo() {
    return "Hola Mundo!"
  }
  console.log(holaMundo())
}

funcionDentroDeFuncion()

function absolute(num) {
  return num > -1 ? num : -num
}

console.log(absolute(4))

var variableGlobal = 33

function imprimeVariableGlobal() {
  console.log(variableGlobal)
  var variableLocal = 33
}

imprimeVariableGlobal()

function imprimeVariableLocal() {
  console.log(variableLocal)
}

imprimeVariableLocal()

function cadenaTextoNumero(cadena1, cadena2) {
  let vecesImpresoNumero = 0

  for (let numero = 1; numero <= 100; numero++) {
    if (numero % 3 === 0 && numero % 5 === 0) {
      console.log(cadena1 + cadena2)
    } else if (numero % 3 === 0) {
      console.log(cadena1)
    } else if (numero % 5 === 0) {
      console.log(cadena2)
    } else {
      console.log(numero)
      vecesImpresoNumero++
    }
  }

  return vecesImpresoNumero
}

cadenaTextoNumero("tonto", "polla")