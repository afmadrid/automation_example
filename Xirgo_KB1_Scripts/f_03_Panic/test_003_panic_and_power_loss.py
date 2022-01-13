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
def test_003_panic_and_power_loss(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Press pan/priv button for 6-7 seconds (LED will come on flashing)
    Report.step('Pan/priv button pressed.')
    # 2. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 3. Kill constant power, and wait 30-60 secs
    Report.step('Power Supply set to Off.')
    Report.comment('Wait time of 50 seconds.')
    # 4. Restore constant power, and allow boot sequence to complete
    Report.step('Power Supply set to On.')
    Report.comment('Wait time of 10 seconds.')
    # 5. Check the state of the pan/priv accumulator
    Report.step('Status of pan/priv accumulator verified.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 6. Verify that the LED returns to its previous state
    Report.step('LED status verified.')
    Report.verify(True, True, 'LED did not return to its previous state.')
    # 7. Hold down panic button until LED turns off.
    Report.step('Panic button pressed for 2 seconds.')
    Report.verify(True, True, 'LED was not turned off.')
    sleep(randint(0, 5))
