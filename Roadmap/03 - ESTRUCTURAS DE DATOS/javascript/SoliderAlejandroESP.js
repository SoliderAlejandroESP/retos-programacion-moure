// Operaciones: Busqueda, inserción, actualización, eliminación, salir
// Contacto formado por un nombre y un número de telefono
// Se pide primero la operación a realizar y luego los datos
// Numeros de telefonos solamente numéricos y menos de una determinada longitud
const readline = require('readline')

const contacts = []

function searchContact () {
  rl.question('¿Cuál es el nombre del contacto a buscar?', contactName => {
    const queryResult = contacts.filter(contact => contact.name === contactName)

    if (!queryResult) {
      console.log(`Error, el contacto ${contactName} no se encuentra en la agenda, por favor, añadelo o busque otro contacto.`)
    }

    console.log(`El contact ${queryResult.name}, tiene como número de telefono el ${queryResult.phone}`)
  })
}

function addContact () {
  rl.question('¿Cuál es el nombre del contacto?', contactName => {
    rl.question('¿Cuál es el número de telefono?', contactPhone => {
      if (contactPhone.length() > 11) {
        console.log('Error, el número del contacto debe contener menos de 12 números')
      } else {
        try {
          const contactPhoneNumber = Number(contactPhone)
          const newContactObject = {
            name: contactName,
            phone: contactPhoneNumber
          }
          contacts.push(newContactObject)
        } catch (error) {
          console.log('Error, el número del contacto debe contener solo números')
        }
      }
    })
  })
}

function updateContact () {

}

function deleteContact () {

}

function startAgenda () {
  const rl = readline.createInterface({
    interface: process.stdin,
    output: process.stdout
  })

  rl.question(`Bienvenido a tu agenda personal. ¿Qué desea realizar?
    - Buscar contacto [1]
    - Añadir contacto [2]
    - Actualizar contacto [3]
    - Eliminar contacto [4]
    - Salir [5]`, opcion => {
      switch (opcion) {
        case '1':
          searchContact()
          break
        case '2':
          addContact()
          break
        case '3':
          updateContact()
          break
        case '4':
          deleteContact()
          break
        case '5':
          rl.close()
      }
    }
  )
  
  rl.on('close', () => {
    console.log('Cerrado agenda')
    process.exit(0)
  })
}