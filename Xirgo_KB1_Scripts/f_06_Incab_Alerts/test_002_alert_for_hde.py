# - Configure test device with the Universal Script and appropriate parameter file
# - Verify desired HDE thresholds using :rycfg aet[0] and :rycfg aet[1]
# - If necessary adjust thresholds
   # - :wycfg aet[0] 0 1000 1000 <mG>  #Accel
   # - :wycfg aet[1] 1 1000 1000 <mG> #Decel
# - Trigger a few HDEs
# - Verify that buzzer triggers when HDE occurs