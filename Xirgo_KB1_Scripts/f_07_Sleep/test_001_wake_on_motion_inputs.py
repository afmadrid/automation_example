# - Power on device and configure sleep timers to 10 minutes for test
   # - 90-sec reporting (RVL-NA, Univ-RVL-M90)
      # - :wycfg tmr[10] 600 0
      # - :wycfg gcv[10] 10
      # - :wycfg gcv[11] 05
      # - :vycfg
   # - 30-sec reporting (NA-IoT, Univ-NA-Iot, Univ-GOV-M30, Univ-RVL-M30)
      # - :wycfg tmr[10] 600 0
      # - :wycfg gcv[10] 20
      # - :wycfg gcv[11] 10
      # - :vycfg
# - Turn ignition on and wait 1-2 minutes
# - Turn ignition off
   # - Use :rrval timer 10 to check current timer state for legacy configs
   # - Use :rrval uservar 2 4 (for sleep timer) and :rrval uservar 2 5 (for daily/periodic plot timer) to check current timer state for the Universal Script
# - Verify that device goes to sleep (no LEDs) after sleep timer has expired
# - Wake the device with ignition on
# - Check the state of the timer 27 ( the delay before sleep timer)
# - Verify the device goes back to sleep after timer 27 expires