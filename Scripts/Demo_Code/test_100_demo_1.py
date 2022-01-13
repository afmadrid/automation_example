import pytest
from allure import severity, severity_level
from time import sleep
from random import randint
from Hardware.power_supply import RigolDP800
from Hardware.relay_usb import Relay16CH
from Hardware.diesel import Diesel
from Hardware.xirgo import Xirgo

@pytest.mark.smoke
@pytest.mark.odometer
@severity(severity_level.CRITICAL)
def test_004_max_rpm(pre_conditions_tc_004):
    print('***************Test Case 4***************')
    rly.enable_disable_relay(1, True)
    rly.enable_disable_relay(3, True)
    dsl.send_RPM(1500)
    sleep(wait_time)
    # TODO Add comments to describe assert
    assert not 300 == xrg.read_vehicle_rpm()

@pytest.fixture
def pre_conditions_tc_004():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 4***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    assert False
    yield
    print('***************Tear Down Test Case 4***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    assert False
    del rly