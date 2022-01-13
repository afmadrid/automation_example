from random import randint
import time

# NOTA: usar este codigo dentro de cada test case para simular un tiempo
# entre 1 y 120 segunds.

value = randint(100, 12000) / 100  # nos regresa un numero entre 1 y 120 segundos
print('Delay de ' + str(value) + ' seg, en progreso')
time.sleep(value)
print('Delay de ' + str(value) + ' seg, terminado')