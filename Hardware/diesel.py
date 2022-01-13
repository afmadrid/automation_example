class Diesel:
    def __init__(self, com_port: str):
        print('Diesel initalized in port ' + com_port)

    def __del__(self):
        pass

    def send_RPM(self, rpm: float):
        print('Diesel RPM set to ' + str(rpm))

