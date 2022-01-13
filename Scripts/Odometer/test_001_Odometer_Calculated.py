import pytest
from allure import severity, severity_level
from time import sleep
from random import randint

@pytest.fixture
def intial_conditions():
    """Initial Conditions that are common for all test cases inside this file
        such as initializing hardware."""
    global random_time
    random_time = randint(2,30)
    print('*****Initial Conditions*****')
    print('Starting Software')

#region Test PreConditions
@pytest.fixture
def tc_001():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    yield
    print('*****Teardown*****')
    print('Closing software')

@pytest.fixture
def tc_002():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    yield
    print('*****Teardown*****')
    print('Closing software')

@pytest.fixture
def preconditions_tc_003():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    yield
    print('*****Teardown*****')
    print('Closing software')

@pytest.fixture
def tc_004():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    yield
    print('*****Teardown*****')
    print('Closing software')

@pytest.fixture
def tc_005():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    yield
    print('*****Teardown*****')
    print('Closing software')

@pytest.fixture
def tc_006():
    print('*****Preconditions******')
    print('Setup power supply to 13.3V')
    print('Set Diesel to 1200 rpm')
    print('Open port COM3, 115200, 01,00')
    yield
    print('*****Teardown*****')
    print('Closing software')
#endregion

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_001_average_calculated_odometer_greater_than_0_for_1_days(intial_conditions, tc_001):
    print('*****Test Case 1*****')
    print('Read calculated odometer')
    sleep(1.5)
    assert True

@pytest.mark.smoke
@severity(severity_level.CRITICAL)
def test_002_average_calculated_odometer_greater_than_0_for_4_days(tc_002):
    print('*****Test Case 2*****')
    print('Read calculated odometer')
    sleep(1)
    assert False

@pytest.mark.regression
@severity(severity_level.NORMAL)
def test_003_average_calculated_odometer_greater_than_0_for_14_days(preconditions_tc_003):
    print('*****Test Case 3*****')
    print('Read calculated odometer')
    sleep(1.8)
    assert True

@pytest.mark.regression
@severity(severity_level.TRIVIAL)
def test_004_delta_calculated_odometer_greater_than_0_for_1_days(tc_004):
    print('*****Test Case 4*****')
    print('Read calculated odometer')
    sleep(1.1)
    assert True

@pytest.mark.blackbox
@severity(severity_level.MINOR)
def test_005_delta_calculated_odometer_greater_than_0_for_4_days(tc_005):
    print('*****Test Case 5*****')
    print('Read calculated odometer')
    sleep(1)
    assert True

# TODO: Run test case
@pytest.mark.blackbox
@severity(severity_level.NORMAL)
def test_006_delta_calculated_odometer_greater_than_0_for_14_days(tc_006):
    print('*****Test Case 6*****')
    print('Read calculated odometer')
    sleep(0.7)
    assert False
