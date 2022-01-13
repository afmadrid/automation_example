import pytest
from allure import severity, severity_level
from time import sleep
from Libraries.toolbox import ToolBox

@pytest.fixture
def intial_conditions():
    """Initial Conditions that are common for all test cases inside this file
        such as initializing hardware."""
    global tbox, pps
    tbox = ToolBox('madal1c', 'St5rtszn')
    # pps = RigolDP800('USB0::0x1AB1::0x0E11::DP8B224001956::INSTR')
    # rly = Relay16CH('COM4')

#region Test PreConditions
@pytest.fixture
def tc_001():
    pass

@pytest.fixture
def tc_002():
    pass

@pytest.fixture
def preconditions_tc_003():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    pass

@pytest.fixture
def tc_004():
    pass

@pytest.fixture
def tc_005():
    pass

@pytest.fixture
def tc_006():
    pass
#endregion


@severity(severity_level.CRITICAL)
def test_001_average_calculated_odometer_greater_than_0_for_1_days(intial_conditions, tc_001):
    print('Test Case 1')
    sleep(2.5)
    assert True

@severity(severity_level.CRITICAL)
def test_002_average_calculated_odometer_greater_than_0_for_4_days(tc_002):
    print('Test case 2')
    sleep(3)
    assert(False, )

@severity(severity_level.NORMAL)
def test_003_average_calculated_odometer_greater_than_0_for_14_days(preconditions_tc_003):
    print('*****Test Case 3*****')
    print('Read calculated odometer')
    sleep(3.8)
    assert True

@severity(severity_level.TRIVIAL)
def test_004_delta_calculated_odometer_greater_than_0_for_1_days(tc_004):
    print('Test Case 4')
    sleep(4.1)
    assert True

@severity(severity_level.MINOR)
def test_005_delta_calculated_odometer_greater_than_0_for_4_days(tc_005):
    print('Test Case 5')
    sleep(7)
    assert True

@severity(severity_level.NORMAL)
def test_006_delta_calculated_odometer_greater_than_0_for_14_days(tc_006):
    print('Test Case 6')
    sleep(0.7)
    assert False
