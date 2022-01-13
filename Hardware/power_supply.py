import pyvisa
from time import sleep


class RigolDP800:
    """Module to control RIGOL Programable Power Supply DP800 series via USB and SCPI commands.
       NI Visa needs to be installed and device to be setup in NI MAX."""

    def __init__(self, instrument_name: str, active_channel: int = 1, pause_time: float = 1) -> None:
        rm = pyvisa.ResourceManager()
        try:
            self._inst = rm.open_resource(instrument_name)
        except pyvisa.errors.VisaIOError:
            raise Exception('Rigol DP800 PPS: "' + instrument_name + '" not found, verify it is connected with USB '
                                                                     'cable and correctly setup in NI MAX.')
        print('Instrument "' + instrument_name + '" initialized.')
        self._pause = pause_time
        self._channel = 0
        self.select_active_channel(active_channel)

    def __repr__(self):
        return 'Module to control RIGOL Programable Power Supply DP800 series via USB and SCPI commands. ' \
               'NI Visa needs to be installed and device to be setup in NI MAX.'

    def __del__(self):
        self._inst.close()

    def select_active_channel(self, active_channel: int) -> None:
        self._inst.write(':INST:SEL CH' + str(active_channel))
        self._channel = active_channel
        sleep(self._pause)
        print('Channel ' + str(self._channel) + ' selected.')

    def turn_on_off_channel(self, status: bool) -> None:
        status_str = 'ON' if status else 'OFF'
        self._inst.write(':OUTP ' + status_str)
        sleep(self._pause + 1)
        print('Channel ' + str(self._channel) + ' turned ' + status_str + '.')

    def measure_voltage(self) -> float:
        voltage = float(self._inst.query(':MEAS:VOLT? CH' + str(self._channel)))
        sleep(self._pause)
        print('Measured voltage in channel ' + str(self._channel) + ' is: ' + str(voltage) + ' V')
        return voltage

    def measure_current(self) -> float:
        current = float(self._inst.query(':MEAS:CURR? CH' + str(self._channel)))
        sleep(self._pause)
        print('Measured current in channel ' + str(self._channel) + ' is: ' + str(current) + ' A')
        return current

    def measure_power(self) -> float:
        power = float(self._inst.query(':MEAS:POWE? CH' + str(self._channel)))
        sleep(self._pause)
        print('Measured power in channel ' + str(self._channel) + ' is: ' + str(power) + ' W')
        return power

    def measure_all(self) -> list:
        result = self._inst.query(':MEAS:ALL? CH' + str(self._channel)).split(',')
        result = [float(i) for i in result]
        sleep(self._pause)
        print('Measured data in channel ' + str(self._channel) + ' is: ' + str(result[0]) + ' V, ' +
              str(result[1]) + ' A, ' + str(result[2]) + ' W')
        return result

    def set_voltage(self, voltage: float) -> None:
        self._inst.write(':VOLT ' + str(voltage))
        sleep(self._pause + 1)
        print('Voltage set to ' + str(voltage) + ' V in channel ' + str(self._channel) + '.')

    def set_current(self, current: float) -> None:
        self._inst.write(':CURR ' + str(current))
        sleep(self._pause + 1)
        print('Current set to ' + str(current) + ' A in channel ' + str(self._channel) + '.')

    def method_test(self):
        return self._inst.query(':OUTP?')

pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
print(pps.method_test())
del pps