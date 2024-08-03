from datetime import datetime

"""
Ejercicio
"""

now = datetime.now()
birthday = datetime(2004, 9, 23, 15, 30, 0, 0)

timeBetween = now - birthday

print(f'{now} - {birthday}: {timeBetween.days // 365} years')


"""
Extra
"""

# Día, mes y año
print(birthday.strftime("%d/%m/%y"))
print(birthday.strftime("%d/%m/%Y"))

# Horas, minutos y segundos
print(birthday.strftime("%H:%M:%S"))

# Día del año
print(birthday.strftime("%j"))

# Día de la semana
print(birthday.strftime("%A"))

# Nombre del mes
print(birthday.strftime("%h"))
print(birthday.strftime("%B"))

# Representación por defecto del locale
print(birthday.strftime("%c"))
print(birthday.strftime("%x"))
print(birthday.strftime("%X"))

# AM/PM
print(birthday.strftime("%p"))