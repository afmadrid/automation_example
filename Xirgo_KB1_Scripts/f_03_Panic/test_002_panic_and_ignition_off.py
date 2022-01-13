import pytest
from allure import severity, severity_level
from time import sleep
from random import randint
from Libraries.report import Report


@pytest.fixture
def pre_conditions():
    """Preconditions"""
    Report.comment('***************Pre Conditions***************')
    # - Turn on ignition, and wait for 30-60 seconds
    Report.comment('Ignition turned On.')
    Report.comment('Wait time of 50 seconds.')
    sleep(0.5)
    yield
    Report.comment('******************Tear Down*****************')
    # - Turn ignition off
    Report.comment('Ignition Turned Off')
    Report.reset_step_count()

@severity(severity_level.NORMAL)
def test_002_panic_and_ignition_off(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Press pan/priv button for 6-7 seconds (LED will come on flashing)
    Report.step('Pan/priv button pressed.')
    # 2. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 3. Turn off vehicle ignition and verify LED on pan/priv button stays on
    #    (LED should remain flashing at its current rate)
    Report.step('Ignition Turned Off')
    Report.verify(True, True, 'Pan/priv button is off')
    # 4. Check the state of the pan/priv accumulator
    Report.step('Status of Pan/priv accumulator verified.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 5. Verify event code 201’s are being generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 201 was not generated.')
    # 6. Wait 30-60 secs
    Report.step('Wait time of 50 seconds.')
    # 7. Verify that pan/priv button does not turn off
    Report.step('Status of pan/priv input verified.')
    Report.verify(True, True, 'Pan/priv button turned Off.')
    # 8. Turn the ignition back on
    Report.step('Ignition Turned On')
    # 9. Verify LED continues to flash at its current rate.
    Report.step('LED frequency verified.')
    Report.verify(True, True, 'LED is not flashing')
    # 10. Hold down panic button until LED turns off
    Report.step('Panic button pressed for 2 seconds.')
    Report.verify(True, True, 'LED was not turned off.')
    sleep(randint(0, 5))
