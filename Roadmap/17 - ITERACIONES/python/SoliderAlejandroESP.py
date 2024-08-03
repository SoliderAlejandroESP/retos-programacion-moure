"""
Ejercicio
"""

for number in range(1, 11):
  print(number)

number = 1
while number < 11:
  print(number)
  number += 1

def count_ten(number=1):
  if number > 10: 
    return
  print(number)
  count_ten(number + 1)

count_ten()