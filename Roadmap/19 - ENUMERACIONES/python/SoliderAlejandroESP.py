from enum import Enum

class Weekday(Enum):
  LUNES = 1
  MARTES = 2
  MIERCOLES = 3
  JUEVES = 4
  VIERNES = 5
  SABADO = 6
  DOMINGO = 7

def get_day(number: int):
    print(Weekday(number).name)


get_day(1)
get_day(3)

"""
Extra
"""

class OrderState(Enum):
  CANCELED = 0
  PENDING = 1
  SENT = 2
  DELIVERED = 3

class Order:
  state = OrderState.PENDING

  def __init__(self, id: int):
    self.id = id
  
  def sent(self):
    if self.state == OrderState.PENDING:
      self.state = OrderState.SENT
    else:
      print('El pedido ya ha sido enviado o cancelado')
  
  def cancel(self):
    if self.state != OrderState.DELIVERED:
      self.state = OrderState.CANCELED
    else:
      print('No se puede cancelar, el envio está Entragado.')
  
  def deliver(self):
    if self.state == OrderState.SENT:
      self.state = OrderState.DELIVERED
    else:
      print('El pedido necesita ser enviado antes de entregarse.')

order = Order(1)
print(order.state)

order.sent()
print(order.state)

order.deliver()
print(order.state)

order.cancel()
print(order.state)
