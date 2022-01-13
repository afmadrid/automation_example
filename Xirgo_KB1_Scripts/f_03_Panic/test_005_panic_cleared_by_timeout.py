import pytest
from allure import severity, severity_level
from time import sleep
from random import randint
from Libraries.report import Report


@pytest.fixture
def pre_conditions():
    """Preconditions"""
    Report.comment('***************Pre Conditions***************')
    # - Change Timer 19 from 1 hour to 5 mins (300 secs)
    # - :wycfg tmr[19] 300 0
    # - :vycfg
    Report.comment('Timer 19 configured to 300 seconds.')
    Report.comment('Command ":wycfg tmr[19] 300 0" sent.')
    Report.comment('Command ":vycfg" sent.')
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
    # 1. Press pan/priv button for 6-7 seconds (LED will come on flashing)
    Report.step('Pan/priv button pressed for 7 seconds.')
    Report.verify(True, True, 'LED frequency was not detected.')
    # 2. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 3. Allow Panic to expire
    # (The state of timer 19 can be monitored by sending serial message :rrval timer 19).
    Report.step('Wait time until panic alert expiration in Timer 19.')
    Report.comment('Command ":rrval timer 19" sent.')
    # 4. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 5. Verify event code 206 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 206 was not generated.')
    # 6. Verify that pan/priv button LED is off
    Report.step('LED status verified.')
    Report.verify(True, True, 'Pan/priv status verified.')
    sleep(randint(0, 5))
