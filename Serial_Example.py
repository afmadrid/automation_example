import serial
from time import sleep

ser = serial.Serial(port='COM6', baudrate=115200)
sleep(2)

data = ':qbi'

ser.write(data.encode())
sleep(0.5)

if ser.in_waiting:
    serial_read = ser.readline().decode('Ascii')
else:
    serial_read = ''

print(serial_read, end='')

ser.close()
