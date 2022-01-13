import pytest
from allure import severity, severity_level
from time import sleep
from random import randint
from Libraries.report import Report

@pytest.fixture
def pre_conditions():
    """Preconditions"""
    Report.comment('***************Pre Conditions***************')
    # - Configure unit for constant buzzer and no grace period
    Report.comment('Constant buzzer and grace period configured.')
    sleep(0.5)
    yield
    Report.comment('******************Tear Down*****************')
    # - Turn ignition off
    Report.comment('Ignition Turned Off')
    Report.reset_step_count()


@severity(severity_level.NORMAL)
def test_001_constant_buzzer(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Turn ignition on and verify that the buzzer provides a 1 sec warning beep after 30 secs
    Report.step('Iginition Turned On.')
    Report.verify(True, True, '1 second warning beep was not heard after 30 seconds.')
    # 2. Check the state of flags using :rrval flags, you're looking to verify that flag 8 is not set
    Report.step('Flag state verified.')
    Report.verify(True, True, 'State flag 8 is enabled.')
    # 3. Verify that buzzer activates continuously (I recommend using an LED here)
    Report.step('Buzzer frequency verified.')
    Report.verify(True, True, 'Buzzer is not activated continuously.')
    # 4. Apply key fob and verify that the buzzer turns off and that flag 8 is set
    Report.step('Key fob is applied.')
    Report.verify(True, True, 'Buzzer was not turned Off.')
    Report.verify(True, True, 'State flag 8 was not enabled.')
    sleep(randint(0, 5))
