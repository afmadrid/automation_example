import pytest
from allure import severity, severity_level
from time import sleep
from random import randint
from Hardware.power_supply import RigolDP800
from Hardware.relay_usb import Relay16CH
from Hardware.diesel import Diesel
from Hardware.xirgo import Xirgo


#region Test PreConditions
@pytest.fixture
def pre_conditions_tc_001():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 1***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 1***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
# TODO: es necesario cambiar el nombre de preconditions
def pre_conditions_tc_002():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 2***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 2***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
@pytest.mark.regression
def pre_conditions_tc_003():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 3***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 3***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

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
    yield
    print('***************Tear Down Test Case 4***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
# TODO: es necesario cambiar el nombre de preconditions
def pre_conditions_tc_005():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 5***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 5***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
@pytest.mark.regression
def pre_conditions_tc_006():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 6***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 6***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
def pre_conditions_tc_007():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 7***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 7***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
# TODO: es necesario cambiar el nombre de preconditions
def pre_conditions_tc_008():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 8***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 8***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
@pytest.mark.regression
def pre_conditions_tc_009():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 9***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 9***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
def pre_conditions_tc_010():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 10***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 10***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
# TODO: es necesario cambiar el nombre de preconditions
def pre_conditions_tc_011():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 11***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 11***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly

@pytest.fixture
@pytest.mark.regression
def pre_conditions_tc_012():
    global wait_time, pps, rly, dsl, xrg
    print('***************Pre Conditions Test Case 12***************')
    wait_time = randint(2, 30)
    pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    rly = Relay16CH('COM4')
    dsl = Diesel('COM5')
    xrg = Xirgo('COM6')
    pps.turn_on_off_channel(True)
    pps.set_voltage(13.5)
    yield
    print('***************Tear Down Test Case 12***************')
    pps.set_voltage(0)
    pps.turn_on_off_channel(False)
    rly.enable_disable_all_relays(False)
    dsl.send_RPM(0)
    del rly
#endregion

@pytest.mark.smoke
@pytest.mark.odometer
@severity(severity_level.CRITICAL)
def test_001_max_rpm(pre_conditions_tc_001):
    print('***************Test Case 1***************')
    rly.enable_disable_relay(1, True)
    rly.enable_disable_relay(3, True)
    dsl.send_RPM(1500)
    sleep(wait_time)
    # TODO Add comments to describe asserts
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_002_avg_rpm(pre_conditions_tc_002):
    print('***************Test Case 2***************')
    rly.enable_disable_relay(2, True)
    rly.enable_disable_relay(4, True)
    dsl.send_RPM(900)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_003_min_rpm(pre_conditions_tc_003):
    print('***************Test Case 3***************')
    rly.enable_disable_relay(3, True)
    rly.enable_disable_relay(5, True)
    dsl.send_RPM(300)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@pytest.mark.odometer
@severity(severity_level.CRITICAL)
def test_004_max_rpm(pre_conditions_tc_004):
    print('***************Test Case 4***************')
    rly.enable_disable_relay(1, True)
    rly.enable_disable_relay(3, True)
    dsl.send_RPM(1500)
    sleep(wait_time)
    # TODO Add comments to describe asserts
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_005_avg_rpm(pre_conditions_tc_005):
    print('***************Test Case 5***************')
    rly.enable_disable_relay(2, True)
    rly.enable_disable_relay(4, True)
    dsl.send_RPM(900)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_006_min_rpm(pre_conditions_tc_006):
    print('***************Test Case 6***************')
    rly.enable_disable_relay(3, True)
    rly.enable_disable_relay(5, True)
    dsl.send_RPM(300)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@pytest.mark.odometer
@severity(severity_level.CRITICAL)
def test_007_max_rpm(pre_conditions_tc_007):
    print('***************Test Case 7***************')
    rly.enable_disable_relay(1, True)
    rly.enable_disable_relay(3, True)
    dsl.send_RPM(1500)
    sleep(wait_time)
    # TODO Add comments to describe asserts
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_008_avg_rpm(pre_conditions_tc_008):
    print('***************Test Case 8***************')
    rly.enable_disable_relay(2, True)
    rly.enable_disable_relay(4, True)
    dsl.send_RPM(900)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_009_min_rpm(pre_conditions_tc_009):
    print('***************Test Case 9***************')
    rly.enable_disable_relay(3, True)
    rly.enable_disable_relay(5, True)
    dsl.send_RPM(300)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@pytest.mark.odometer
@severity(severity_level.CRITICAL)
def test_010_max_rpm(pre_conditions_tc_010):
    print('***************Test Case 10***************')
    rly.enable_disable_relay(1, True)
    rly.enable_disable_relay(3, True)
    dsl.send_RPM(1500)
    sleep(wait_time)
    # TODO Add comments to describe asserts
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_011_avg_rpm(pre_conditions_tc_011):
    print('***************Test Case 11***************')
    rly.enable_disable_relay(2, True)
    rly.enable_disable_relay(4, True)
    dsl.send_RPM(900)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_012_min_rpm(pre_conditions_tc_012):
    print('***************Test Case 12***************')
    rly.enable_disable_relay(3, True)
    rly.enable_disable_relay(5, True)
    dsl.send_RPM(300)
    sleep(wait_time)
    assert not 1500 == xrg.read_vehicle_rpm()
