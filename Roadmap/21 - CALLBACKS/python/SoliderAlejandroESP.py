import time
import random

"""
Ejercicio
"""

def funcion_primaria(name: str, callback):
  print('Esta función ejecutará una función de saludo cuando termine.')
  callback(name)

def funcion_saludo(name: str):
  print(f'Hola, {name}! Soy el callback y he sido ejecutado cuando se finaliza la ejecución de una función')

funcion_primaria("Alejandro", funcion_saludo)

"""
Extra
"""

def simulador_pedidos(pedido: str, callback_confirmado, callback_enviado, callback_entregado):
  def procesar():
    callback_confirmado(pedido)
    time.sleep(random.randint(1, 10))
    callback_enviado(pedido)
    time.sleep(random.randint(1, 10))
    callback_entregado(pedido)
  procesar()    


def pedido_confirmado(pedido: str):
  print(f'Tu pedido {pedido} se ha confirmado.')

def pedido_enviado(pedido: str):
  print(f'Tu pedido {pedido} se ha enviado.')

def pedido_entregado(pedido: str):
  print(f'Tu pedido {pedido} se ha entregado.')

simulador_pedidos("Almejas", pedido_confirmado, pedido_enviado, pedido_entregado)
simulador_pedidos("Patacas", pedido_confirmado, pedido_enviado, pedido_entregado)
simulador_pedidos("Chochos (altramuces mercadona)", pedido_confirmado, pedido_enviado, pedido_entregado)
