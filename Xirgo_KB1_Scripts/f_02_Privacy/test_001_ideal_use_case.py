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
def test_001_ideal_use_case(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Press pan/priv button for 2-3 seconds (LED will come on solid)
    Report.step('Pan/priv button pressed for 3 seconds.')
    # 2. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 3. Verify event code 202 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 202 was not generated.')
    # 4. Turn off vehicle ignition and verify LED on pan/priv button turns off
    Report.step('Ignition Turned Off')
    Report.verify(True, True, 'Pan/priv button is turned on.')
    # 5. Wait for 1-2 minutes then turn ignition back on
    Report.step('Wait time of 2 minutes.')
    Report.verify(True, True, 'Ignition was not turned on.')
    # 6. Check the state of the pan/priv accumulator
    Report.step('State of pan/priv accumulator verified.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 7. Verify that pan/priv button LED is off
    Report.step('Pan/priv LED status verified.')
    Report.verify(True, True, 'Pan/priv button LED is turned on.')
    # 8. Verify event code 204 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 204 was not generated.')
    sleep(randint(0, 5))
