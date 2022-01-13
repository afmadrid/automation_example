import random


class Xirgo:
    def __init__(self, com_port):
        print('Xirgo initialized in port: ' + com_port)

    def read_vehicle_rpm(self):
        i = random.randint(0, 2)
        rpm = [300, 900, 1500]
        print('RPM measured from Xirgo are: ' + str(rpm[i]))
        return rpm[i]