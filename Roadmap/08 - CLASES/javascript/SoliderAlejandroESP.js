class Ejemplo {
  constructor(atributo1, atributo2) {
    this.atributo1 = atributo1
    this.atributo2 = atributo2
  }

  imprimirAtributos() {
    console.log(this.atributo1, this.atributo2)
  }
}

let ejemplo1 = new Ejemplo("Hola", "Mundo!")

ejemplo1.imprimirAtributos()

ejemplo1.atributo1 = "Adios"
ejemplo1.atributo2 = "Luna!"

ejemplo1.imprimirAtributos()

class Pila {
  constructor() {
    this.stack = []
  }

  introducir(elemento) {
    this.stack.push(elemento)
  }

  quitar() {
    return this.stack.pop()
  }

  ultimoElemento() {
    this.stack[this.stack.length - 1]
  }

  imprimirPila() {
    console.log(this.stack)
  }
}

class Cola {
  constructor() {
    this.queue = []
  }

  introducir(elemento) {
    this.queue.push(elemento)
  }

  quitar() {
    return this.queue.shift()
  }

  ultimoElemento() {
    this.queue[this.queue.length - 1]
  }

  imprimirCola() {
    console.log(this.queue)
  }
}

const pila = new Pila()
pila.imprimirPila()
pila.introducir("Hola")
pila.introducir("Mundo!")
pila.imprimirPila()
pila.quitar()
pila.imprimirPila()

const cola = new Cola()
cola.imprimirCola()
cola.introducir("Hola")
cola.introducir("Mundo!")
cola.imprimirCola()
cola.quitar()
cola.quitar()
cola.imprimirCola()