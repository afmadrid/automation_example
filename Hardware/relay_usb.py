import serial
from time import sleep

class Relay16CH:
    def __init__(self, com_port, baud_rate=11520):
        self._ser = serial.Serial(port=com_port, baudrate=baud_rate)
        print('USB 16 Channels Relay card opened in port ' + com_port + ' with baudrate of ' + str(baud_rate))


        self._channel_serial_data = {
            'CH-1 ON':   '3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A',
            'CH-1 OFF':  '3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A',
            'CH-2 ON':   '3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A',
            'CH-2 OFF':  '3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A',
            'CH-3 ON':   '3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A',
            'CH-3 OFF':  '3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A',
            'CH-4 ON':   '3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A',
            'CH-4 OFF':  '3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A',
            'CH-5 ON':   '3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A',
            'CH-5 OFF':  '3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A',
            'CH-6 ON':   '3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A',
            'CH-6 OFF':  '3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A',
            'CH-7 ON':   '3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A',
            'CH-7 OFF':  '3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A',
            'CH-8 ON':   '3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A',
            'CH-8 OFF':  '3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A',
            'CH-9 ON':   '3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A',
            'CH-9 OFF':  '3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A',
            'CH-10 ON':  '3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A',
            'CH-10 OFF': '3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A',
            'CH-11 ON':  '3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A',
            'CH-11 OFF': '3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A',
            'CH-12 ON':  '3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A',
            'CH-12 OFF': '3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A',
            'CH-13 ON':  '3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A',
            'CH-13 OFF': '3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A',
            'CH-14 ON':  '3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A',
            'CH-14 OFF': '3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A',
            'CH-15 ON':  '3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A',
            'CH-15 OFF': '3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A',
            'CH-16 ON':  '3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A',
            'CH-16 OFF': '3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A'
        }

    def __repr__(self):
        return 'Module to control USB 16 Channels Relay card.'

    def __del__(self):
        self._ser.close()

    def enable_disable_relay(self, relay_number: int, status_on_off: bool) -> None:
        try:
            channel_key = 'CH-' + str(relay_number) + ' ' + ('ON' if status_on_off else 'OFF')
            serial_data = self._channel_serial_data[channel_key]
            print('Relay ' + str(relay_number) + ' was ' + ('enabled' if status_on_off else 'disabled') + '.')
            self._write_serial(serial_data)
            print('Serial data sent: ' + chr(10) + serial_data)
        except KeyError:
            print('Relay ' + str(relay_number) + ' does not exist, select a number between 1 and 16.')

    def enable_disable_all_relays(self, status_on_off: bool) -> None:
        print('All relays where ' + ('enabled' if status_on_off else 'disabled') + '.')
        if status_on_off:
            serial_data = '3A 46 45 30 46 30 30 30 30 30 30 31 30 30 32 46 46 46 46 45 33 0D 0A'
        else:
            serial_data = '3A 46 45 30 46 30 30 30 30 30 30 31 30 30 32 30 30 30 30 45 31 0D 0A'
        self._write_serial(serial_data)
        print('Serial data sent: ' + chr(10) + serial_data)

    def read_relay_status(self) -> None:
        serial_data = '3A 46 45 30 31 30 30 30 30 30 30 31 30 46 31 0D 0A'
        self._write_serial(serial_data)
        print('Serial data sent: ' + chr(10) + serial_data)

    def read_relay_status_return_value(self) -> None:
        serial_data = '3A 46 45 30 31 30 30 32 30 30 30 30 30 46 46 0D 0A'
        self._write_serial(serial_data)
        print('Serial data sent: ' + chr(10) + serial_data)

    def _write_serial(self, data: str):
        self._ser.write(data.encode())
        sleep(0.2)

    def _read_serial(self):
        if self._ser.in_waiting:
            return self._ser.readline().decode('Ascii')
        else:
            return ''

