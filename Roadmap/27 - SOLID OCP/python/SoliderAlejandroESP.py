"""
Ejercicio
"""

# Incorrecta
class Form:
  
  def draw(self):
    print('Dibujar una forma geometrica')
  
  def draw_circle(self):
    print('Dibujar un circulo')

# Correcta

from abc import ABC, abstractmethod

class Form:
  @abstractmethod
  def draw(self):
    pass

class Square(Form):
  def draw(self):
    print('Dibujar un cuadrado')

class Circle(Form):
  def draw(self):
    print('Dibuja un circulo')

class Triangle(Form):
  def draw(self):
    print('Dibuja un triangulo')


"""
Extra
"""

class Operation(ABC):
  @abstractmethod
  def execute(self, a, b):
    pass

class Addition(Operation):
  def execute(self, a, b):
    return a + b

class Sustract(Operation):
  def execute(self, a, b):
    return a - b

class Multiply(Operation):
  def execute(self, a, b):
    return a * b

class Division(Operation):
  def execute(self, a, b):
    return a / b

class Power(Operation):
  def execute(self, a, b):
    return a ** b

class Calculator:
  def sum(self, a, b):
    return Addition().execute(a, b)
  
  def substract(self, a, b):
    return Sustract().execute(a, b)
  
  def multiply(self, a, b):
    return Multiply().execute(a, b)
  
  def divide(self, a, b):
    return Division().execute(a, b)
  
  def power(self, a, b):
    return Power().execute(a, b)

calc = Calculator()
print(calc.sum(2, 2))
print(calc.substract(2, 1))
print(calc.multiply(3, 3))
print(calc.divide(5, 2))
print(calc.power(2, 16))