import unittest
from datetime import date

from Battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_need_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-02-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.need_service())
        
    def test_need_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-02-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.need_service())