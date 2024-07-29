function recursividadNumeros(numero) {
  console.log(numero)
  if (numero > 0) {
    recursividadNumeros(numero - 1)
  }
}

recursividadNumeros(100)

function factorial(n) {
  if (n <= 1) {
    return 1
  }
  return n * factorial(n - 1)
}

console.log(factorial(5))

function fibonacci(n) {
  if (n <= 1) {
    return n
  }
  return fibonacci(n - 1) + fibonacci(n - 2)
}

console.log(fibonacci(13))