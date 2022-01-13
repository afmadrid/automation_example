import serial
from time import sleep
import keyboard as key


def write_ser_char_on_key_input() -> bool:
    while True:
        if key.is_pressed('a'):
            ser.write('a'.encode())
            return False
        elif key.is_pressed('d'):
            ser.write('d'.encode())
            return False
        elif key.is_pressed('s'):
            ser.write('s'.encode())
            return False
        elif key.is_pressed('w'):
            ser.write('w'.encode())
            return False
        elif key.is_pressed('e'):
            ser.write('e'.encode())
            return False
        elif key.is_pressed('f'):
            ser.write('f'.encode())
            return False
        elif key.is_pressed('x'):
            return True
        else:
            pass


ser = serial.Serial(port='COM8', baudrate='115200')
sleep(3)
stop = False

while not stop:
    stop = write_ser_char_on_key_input()
    sleep(0.2)
    if ser.in_waiting:
        ser_line = ser.readline()
        print(ser_line.decode('Ascii'), end='')

ser.close()




