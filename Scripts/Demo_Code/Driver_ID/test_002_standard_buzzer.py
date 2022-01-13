import pytest
from allure import severity, severity_level
from time import sleep
from random import randint
from Libraries.report import Report


@pytest.fixture
def pre_conditions():
    """Preconditions"""
    Report.comment('***************Pre Conditions***************')
    # - Configure unit for 10 min grace period and 5 min buzzer
    Report.comment('Buzzer configured for 5 minutes.')
    Report.comment('Unit configured for 10 minutes grace period.')
    sleep(0.5)
    yield
    Report.comment('******************Tear Down*****************')
    # - Turn ignition off
    Report.comment('Ignition Turned Off')

@severity(severity_level.NORMAL)
def test_002_standard_buzzer(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Turn ignition on and verify that the buzzer provides a 1 sec warning beep after 30 secs
    Report.step('Iginition Turned On')
    Report.verify(True, True, '1 second warning beep was not heard after 30 seconds.')
    # 2. Check the state of flags using :rrval flags, you're looking to verify that flag 8 is not set
    Report.step()
    Report.verify(True, True, 'State flag 8 is enabled.')
    # 3. Verify that buzzer times out after 5 minutes (I recommend using an LED here)
    Report.step('Wait time of 5 minutes.')
    Report.verify(True, True, 'Buzzer did not time out after 5 minutes.')
    # 4. Apply key fob and verify that the buzzer turns off and that flag 8 is set
    Report.step('Key fob is applied.')
    Report.verify(True, True, 'Buzzer was not turned Off.')
    Report.verify(True, True, 'State flag 8 was not enabled.')
    # 5. Kill ignition for 2-3 mins, then start ignition again
    Report.step('Iginition Turned Off.')
    Report.comment('Wait time of 2.5 minutes.')
    Report.comment('Iginition Turned Off.')
    # 6. Check that flag 8 is still set
    Report.step()
    Report.verify(True, True, 'Status flag 8 is not set.')
    # 7. Verify that the buzzer does not activate
    Report.step()
    Report.verify(True, True, 'Buzzer is enabled.')
    sleep(randint(0, 5))

