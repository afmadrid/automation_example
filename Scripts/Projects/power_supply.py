from Hardware.power_supply import RigolDP800
import logging

pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR', active_channel=1)
#pps.set_voltage(12)
pps.turn_on_off_channel(True)

