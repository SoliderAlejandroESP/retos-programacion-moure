import os
import xml.etree.ElementTree as xml
import json

json_file = "12.json"
xml_file = '12.xml'

info = {
  "nombre": "Alejandro Box",
  "edad": 19,
  "nacimiento": "23/09/2004",
  "lenguajes": "python, c#, c++, HolyC"
}
json_info = json.dumps(info)

with open(json_file, "w") as file:
  file.write(json_info)

with open(json_file, "r") as file:
  print(file.readlines())

os.remove(json_file)