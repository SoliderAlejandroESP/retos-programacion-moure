from functools import reduce
from datetime import datetime

"""
Ejercicio
"""

def apply_func(func, x):
  return func(x)

x = apply_func(len, "Alejandro")
print(x)

def apply_multiplier(n):
  def multiplier(x):
    return x * n
  return multiplier

multiplier_by_2 = apply_multiplier(2)
print(multiplier_by_2(5))

# Sistema

numbers = [1, 3, 4, 2, 5]

# map()

def apply_double(n):
  return n * 2

print(list(map(apply_double, numbers)))

# filter()

def apply_condition(n):
  return n % 2

print(list(filter(apply_condition, numbers)))

# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()

def sum_values(x, y):
  return x + y

print(reduce(sum_values, numbers))

"""
Extra
"""

students = [
  {
    "name": "Alejandro", 
    "birthdate": "23/09/2004", 
    "grades": [5, 8.5, 3, 10]
  },
  {
    "name": "Antonio", 
    "birthdate": "24/04/1998", 
    "grades": [1, 9, 5, 11]
  },
  {
    "name": "Segura", 
    "birthdate": "25/12/2015", 
    "grades": [9, 9, 9, 9]
  }
]

def average_grades(grades):
  return sum(grades) / len(grades)

print(list(map(lambda student: {"name": student["name"], "average": average_grades(student['grades'])}, students)))

print(list(map(lambda student: {"name": student["name"]}, filter(lambda student: average_grades(student["grades"]) >= 9, students))))

print(sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%d/%m/%Y"), reverse=True))

print(max(map(lambda student: max(student["grades"]), students)))
