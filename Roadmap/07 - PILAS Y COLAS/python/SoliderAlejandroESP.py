def web_navigation():
  webStack = []

  while True:
    user_choice = input('Inserte una pagina web o uno de los siguientes comandos disponibles: atrás, adelante, salir: ')
    
    if user_choice == 'salir':
      print('Saliendo del navegador web.')
      break
    elif user_choice == 'adelante':
      pass
    elif user_choice == 'atrás':
      if len(webStack) > 0:
        webStack.pop()
    else:
      webStack.append(user_choice)
    
    if len(webStack) > 0:
      print(f'Has navegado a la pagina: {webStack[len(webStack) - 1]}')
    else:
      print('Estas en la pagina principal.')

web_navigation()

def shared_printed():
  printerQueue = []

  while True:
    user_choice = input('Añade un documento o selecciona imprimir/salir: ')

    if user_choice == 'salir':
      break
    elif user_choice == 'imprimir':
      if len(printerQueue) > 0:
        print(f'Imprimiendo {printerQueue.pop(0)}')
    else:
      printerQueue.append(user_choice)
    
    print(f'Cola de impresion: {printerQueue}')

shared_printed()