import unittest
from datetime import date 

from Battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_need_service_true(self):
        current_date = date.isoformat("2020-05-20")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.need_service())
        
        
    def test_need_service_false(self):
        current_date = date.isoformat("2020-05-20")
        last_service_date = date.fromisoformat("2019-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.need_service())