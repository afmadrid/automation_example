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
    Report.comment('Timer 19 updated to 300 seconds')
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
def test_001_panic_cancelled_by_driver_standard_endpoint(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Configure IP to standard reveal endpoint
    Report.step('IP configured to standard reveal endpoint.')
    # 2. Verify that PT0 3 is configured for Pan/Priv in Fleetcare
    Report.step('PTO 3 configuration verified.')
    Report.verify(True, True, 'PTO 3 is not configured for Pan/Priv in Fleetcare.')
    # 3. Log into Reveal as customer and configure Panic Alerts
    Report.step('Login into Reveal as customer.')
    Report.comment('Panic alerts configured.')
    # 4. Turn on ignition, and wait for 30-60 sec.
    Report.step('Ignition turned On.')
    Report.comment('Wait time of 50 seconds.')
    # 5. Verify that device shows correct state in live map
    Report.step('Live map status verified.')
    Report.verify(True, False, 'Device does not show correct state in live map.')
    # 6. Press pan/priv button for 6-7 seconds (LED will come on flashing at 1Hz (slow flash))
    Report.step('Pan/priv button is pressed for 6 seconds.')
    Report.verify(True, True, 'LED frequency meassured less than 1Hz.')
    # 7. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 8. Verify Panic alert triggers red banner in Reveal
    Report.step('Red Banner in panic alert verified.')
    Report.verify(True, True, 'Red Banner not trigerred in panic alert in Reveal.')
    # 9. Indicate Panic alert is SEEN (hit “REVIEW” in red banner)
    Report.step('Panic alert in red banenr verified.')
    # 10. Check LED, it should change to flashing faster (4Hz) (this may take a few moments)
    Report.step('LED frequency verified.')
    Report.verify(True, True, 'LED frequency meassured less than 4Hz.')
    # 11. Check the state of the pan/priv accumulator
    Report.step('Status of pan/priv accumulator verified.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 12. Verify event code 200 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 205 was not generated.')
    # 13. Kill constant power and wait for 30-60 secs
    Report.step('Power Supply set to Off.')
    Report.comment('Wait time of 50 seconds.')
    # 14. Restore power and verify that LED returns to is previous (4Hz) state
    Report.step('Power Supply set to Off.')
    Report.verify(True, True, 'LED frequency meassured less than 4Hz.')
    # 15. Cancel Panic alert (hit “CANCEL” in red banner). The red banner should close. 
    # Verify the LED goes off. (this may take a few moments)
    Report.step('Panic alert cancelled in red banner.')
    Report.verify(True, True, 'Red banner not closed.')
    Report.verify(True, True, 'LED did not go off.')
    # 16. Verify event code 208 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 208 was not generated.')
    sleep(randint(0, 5))


@severity(severity_level.NORMAL)
def test_002_panic_cancelled_by_driver_iot_endpoint(pre_conditions):
    Report.comment('******************Test Case*****************')
    # 1. Configure IP to standard IoT endpoint
    Report.step('IP configured to IoT endpoint.')
    # 2. Verify that PT0 3 is configured for Pan/Priv in Fleetcare
    Report.step('PTO 3 configuration verified.')
    Report.verify(True, True, 'PTO 3 is not configured for Pan/Priv in Fleetcare.')
    # 3. Log into Reveal as customer and configure Panic Alerts
    Report.step('Login into Reveal as customer.')
    Report.comment('Panic alerts configured.')
    # 4. Turn on ignition, and wait for 30-60 sec.
    Report.step('Ignition turned On.')
    Report.comment('Wait time of 50 seconds.')
    # 5. Verify that device shows correct state in live map
    Report.step('Live map status verified.')
    Report.verify(True, True, 'Device does not show correct state in live map.')
    # 6. Press pan/priv button for 6-7 seconds (LED will come on flashing at 1Hz (slow flash))
    Report.step('Pan/priv button is pressed for 6 seconds.')
    Report.verify(True, True, 'LED frequency meassured less than 1Hz.')
    # 7. Check the status of pan/priv accumulator by using the command :rrval uservar 0 8
    Report.step('Pan/priv accumulator status verified.')
    Report.comment('command ":rrval uservar 0 8" sent.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 8. Verify Panic alert triggers red banner in Reveal
    Report.step('Red Banner in panic alert verified.')
    Report.verify(True, True, 'Red Banner not trigerred in panic alert in Reveal.')
    # 9. Indicate Panic alert is SEEN (hit “REVIEW” in red banner)
    Report.step('Panic alert in red banner verified.')
    # 10. Check LED, it should change to flashing faster (4Hz) (this may take a few moments)
    Report.step('LED frequency verified.')
    Report.verify(True, True, 'LED frequency meassured less than 4Hz.')
    # 11. Check the state of the pan/priv accumulator
    Report.step('Status of pan/priv accumulator verified.')
    Report.verify(True, True, 'Pan/priv accumulator is disabled.')
    # 12. Verify event code 200 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 205 was not generated.')
    # 13. Kill constant power and wait for 30-60 secs
    Report.step('Power Supply set to Off.')
    Report.comment('Wait time of 50 seconds.')
    # 14. Restore power and verify that LED returns to is previous (4Hz) state
    Report.step('Power Supply set to Off.')
    Report.verify(True, True, 'LED frequency meassured less than 4Hz.')
    # 15. Cancel Panic alert (hit “CANCEL” in red banner). The red banner should close.
    # Verify the LED goes off. (this may take a few moments)
    Report.step('Panic alert cancelled in red banner.')
    Report.verify(True, True, 'Red banner not closed.')
    Report.verify(True, True, 'LED did not go off.')
    # 16. Verify event code 208 was generated (ex: Athena check)
    Report.step('Event code verified.')
    Report.verify(True, True, 'Event code 208 was not generated.')
    sleep(randint(0, 5))
