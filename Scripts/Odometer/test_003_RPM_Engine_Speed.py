"""@TID_0007_RPM_Engine_Speed.py

    Test sequence based on - Testrail steps - to cover these test cases:
​
        /===================== Test name ===================/== TID ==/
        * RPM Engine Speed                                   TID 0007
​
    Tranmitted *.per files:
​
        30 RPM
        * ./J1939_TID_0007_RPM_Engine_Speed_30.per

        2000 RPM
        * ./J1939_TID_0007_RPM_Engine_Speed_2000.per
​
        8032 RPM
        * ./J1939_TID_0007_RPM_Engine_Speed_8032.per
​
    Required Instruments:
        * Saint2 (Serial comm)
        * Power Supply - Agilent E3648A (Serial comm)
​
    Required Framework libs:
        * Saint2 Process                    -->     Transmit file
        * Shell                             -->     Log tail -F <log/current_vcore>
        * ADB Commands                      -->     Log CaReader
​
    Estimated test time:
        * 20 minutes
"""
import __global__
​
from instruments.saint2 import Saint2_Process
from instruments.power_supply import power_supply
from utils.adb.vt400 import vt400_commands
from utils import test, timing, output
​
import unittest
import time
import sys
import os
​
log = test.log(__name__)


class VT400_Test(unittest.TestCase):
    ​

    @classmethod
    def setUpClass(self):
        test.begin(__name__)

    ​
    """ VT400 params """
    self.vt400 = vt400_commands()
    ​
    """ Saint2 process """
    self.saint2 = Saint2_Process()
    ​
    """ *.per filepaths """
    _pers_folder = os.path.join(os.path.dirname(__file__), 'per_files')
    _per = lambda f: os.path.join(_pers_folder, f)
    ​
    self.rpm_30 = _per('J1939_TID_0007_RPM_Engine_Speed_30.per')
    ​
    self.rpm_2000 = _per('J1939_TID_0007_RPM_Engine_Speed_2000.per')
    ​
    self.rpm_8032 = _per('J1939_TID_0007_RPM_Engine_Speed_8032.per')

    ​
    """ Start Logging - CaReader """
    self.vt400.logging(True, log_name=__name__)

    # This is intented to run CarReader Telnet & vCore logging processes

    @classmethod
    def tearDownClass(self):
        """ Stop logging - ADB Shell for vCore """
        self.vt400.logging(False)

    ​
    test.end()

    @log.step
    def test_step_001(self, name='Transmit 2000 RPM'):
        self.saint2.transmit(self.rpm_2000)
        timing.wait_for(minutes=5)

    ​
    self.saint2.stop_transmission()

    @log.step
    def test_step_002(self, name='Transmit 8032 RPM'):
        self.saint2.transmit(self.rpm_8032)
        timing.wait_for(minutes=5)

    ​
    self.saint2.stop_transmission()

    @log.step
    def test_step_003(self, name='Transmit 30 RPM'):
        self.saint2.transmit(self.rpm_30)
        timing.wait_for(minutes=5)

    ​
    # SET BATTERY VOLTAGE TO 12 - Key OFF
    output.write(__name__, ' -- Key OFF -- ')
    power_supply.set_voltage(12)
    timing.wait_for(minutes=5)
    ​
    # Wait until ignition OFF is reached...
    ​
    # SET BATTERY VOLTAGE TO 15V - KEY ON
    output.write(__name__, ' -- Key ON -- ')
    power_supply.set_voltage(15)
    timing.wait_for(minutes=1)
    ​
    self.saint2.stop_transmission()