import re

"""
Ejercicio
"""

input_string = input('Inserte la cadena de texto: ')

print(re.findall(r"\d", input_string))


"""
Extra
"""

regex_email = r"[\w]+@gmail\.com"
regex_phone = r"^\+?\d{3}\d{9}"
regex_url = r"http[s]?://[a-zA-Z0-9]+\.com"