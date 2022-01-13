import pytest
from allure import severity, severity_level
from time import sleep

@pytest.fixture
def intial_conditions():
    """Initial Conditions that are common for all test cases inside this file
        such as initializing hardware."""
    pass

#region Test PreConditions
@pytest.fixture
def tc_001():
    pass

@pytest.fixture
def tc_002():
    pass
#endregion

@severity(severity_level.CRITICAL)
def test_001_average_vinvox_odometer_greater_than_0(intial_conditions, tc_001):
    print('Test Case 1')
    sleep(2)
    pass

@severity(severity_level.CRITICAL)
def test_002_delta_vinvox_odometer_greater_than_0(intial_conditions, tc_002):
    print('Test case 2')
    sleep(2.8)
    pass