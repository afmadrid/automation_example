# - Power on device and configure sleep timers for test.
# - Turn ignition on and wait 1-2 minutes
# - Kill ignition
   # - Use :rrval timer 10 to check current timer state for legacy configs 
   # - Use :rrval uservar 2 4 (for sleep timer) and :rrval uservar 2 5 (for daily/periodic plot timer) to check current timer state for the Universal Script
# - Verify that device goes to sleep (no LEDs) after sleep timer has expired
# - Kill constant power, and wait 30-60 secs
# - Restore constant power
# - Check the state of the timer 27 ( the delay before sleep timer)
# - Verify the device goes back to sleep after timer 27 expires