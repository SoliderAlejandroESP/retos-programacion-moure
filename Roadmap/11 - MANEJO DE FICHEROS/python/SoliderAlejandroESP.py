import os

"""
Ejercicio
"""

file_name = "SoliderAlejandroESP.txt"

with open(file_name, "w") as file:
  file.write("Alejandro\n")
  file.write("19\n")
  file.write("Python")

with open(file_name, "r") as file:
  print(file.read())

os.remove(file_name)

"""
Extra
"""

# [nombre_producto], [cantidad vendida], [precio]

file_name = "ventas.txt"

while True:
  print("1. Añadir producto")
  print("2. Consultar producto")
  print("3. Actualizar producto")
  print("4. Borrar producto")
  print("5. Mostrar productos")
  print("6. Calcular venta total")
  print("7. Calcular venta por producto")
  print("8. Salir")

  option = int(input("Selecciona una opción: "))

  if option == 1:
    name = input("Nombre: ")
    quantity = input("Cantidad: ")
    price = input("Precio: ")
    with open(file_name, "a") as file:
      file.write(f'{name}, {quantity}, {price}')
  elif option == 2:
    name = input("Nombre: ")
    with open(file_name, "r") as file:
      for line in file.readlines():
        if line.split(', ')[0] == name:
          print(line)
          break
  elif option == 3:
    name = input("Nombre: ")
    quantity = input("Cantidad: ")
    price = input("Precio: ")
    with open(file_name, "r") as file:
      lines = file.readlines()
    with open(file_name, "w") as file:
      for line in lines:
        if line.split(", ")[0] == name:
          file.write(f"{name}, {quantity}, {price}\n")
        else:
          file.write(line)
  elif option == 4:
    name = input("Nombre: ")
    with open(file_name, "r") as file:
      lines = file.readlines()
    with open(file_name, "w") as file:
      for line in lines:
        if line.split(", ")[0] != name:
          file.write(line)
  elif option == 5:
    with open(file_name, "r") as file:
      print(file.read())
  elif option == 6:
    total = 0
    with open(file_name, "r") as file:
      for line in file.readlines():
        atributes = line.split(', ')
        quantity = atributes[1]
        price = atributes[2]
        total += quantity * price
    print(total)
  elif option == 7:
    name = input("Nombre: ")
    total = 0
    with open(file_name, "r") as file:
      for line in file.readlines():
        atributes = line.split(', ')
        if atributes[0] == name:
          quantity = atributes[1]
          price = atributes[2]
          total += quantity * price
    print(total)
  elif option == 8:
    os.remove(file_name)
    break
  else:
    print("Selecciona una de las opciones disponibles.")