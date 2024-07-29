class Animal {
  constructor(sonido) {
    this.sonido = sonido
  }

  hacerSonido() {
    console.log(this.sonido)
  }
}

class Perro extends Animal {
  constructor(sonido) {
    super(sonido)
  }
}

class Gato extends Animal {
  constructor(sonido) {
    super(sonido)
  }
}

const gato = new Gato("miau")
const perro = new Perro("ISHOWSPEED!!!")

gato.hacerSonido()
perro.hacerSonido()


class Empleado {
  constructor(id, nombre) {
    this.id = id
    this.nombre = nombre
  }
}

class Gerente extends Empleado {
  constructor(id, nombre, programadores) {
    super(id, nombre)
    this.programadores = programadores
  }

  imprimirProgramadores() {
    console.log(this.programadores)
  }
}

class GerenteProyectos extends Empleado {
  constructor(id, nombre, proyectos) {
    super(id, nombre)
    this.proyectos = proyectos
  }

  imprimirProyectos() {
    console.log(this.proyectos)
  }
}

class Programadores extends Empleado {
  constructor(id, nombre, proyecto) {
    super(id, nombre)
    this.proyecto = proyecto
  }

  imprimirProyecto() {
    console.log(this.proyecto)
  }
}