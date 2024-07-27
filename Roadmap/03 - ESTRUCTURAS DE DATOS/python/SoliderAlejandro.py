contacts = {}

def searchContact():
  contactName = input('Inserte el nombre del contact: ')

  if not contactName in contacts.keys():
    print(f'El contacto {contactName} no se encuentra en la agenda')
  else:
    print(f'El contacto {contactName} tiene el número {contacts[contactName]}')

def validPhone(contactPhone):
  if not contactPhone.isdecimal:
    print(f'El número {contactPhone} no es valido, debe de ser solo números')
    return False
  elif len(contactPhone) > 11:
    print(f'El número {contactPhone} no es valido, debe de ser menos de 12 caracteres')
    return False
  return True

def addContact():
  contactName = input('Inserte el nombre del contacto: ')

  if contactName in contacts.keys():
    print(f'El contacto {contactName} ya se encuentra en la agenda')
  else:
    contactPhone = input('Inserte el número del contacto: ')

    if validPhone(contactPhone):
      contacts[contactName] = contactPhone
      print(f'El contacto {contactName} con el telefono {contactPhone} se ha añadido en la agenda')

def updateContact():
  contactName = input('Inserte el nombre del contacto: ')

  if not contactName in contacts.keys():
    print(f'El contacto {contactName} no se encuentra en la agenda')
  else:
    contactNewName = input('Inserte el nuevo nombre: ')
    contactNewPhone = input('Inserte el nuevo telefono: ')
    if validPhone(contactNewPhone):
      contacts.pop(contactName)
      contacts[contactNewName] = contactNewPhone
      print(f'El contacto {contactName} se ha actualizado con el nombre de {contactNewName} y el telefono {contactNewPhone}')

def deleteContact():
  contactName = input('Inserte el nombre del contacto: ')

  if not contactName in contacts.keys():
    print(f'El contacto {contactName} no se encuentra en la agenda')
  else:
    contacts.pop(contactName)
    print(f'El contacto {contactName} se ha borrado de la agenda')

while 1:
  print(contacts)
  option = int(input("""Bienvenido a tu agenda personal. ¿Qué desea realizar?
  - Buscar contacto [1]
  - Añadir contacto [2]
  - Actualizar contacto [3]
  - Eliminar contacto [4]
  - Salir [5]
"""))
  
  if option == 1:
    searchContact()
  elif option == 2:
    addContact()
  elif option == 3:
    updateContact()
  elif option == 4:
    deleteContact()
  elif option == 5:
    break
  else:
    print('Esa opción no existe, porfavor, inserte una valida.')

print('Cerrando agenda.')
