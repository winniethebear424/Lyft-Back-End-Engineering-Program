import unittest

from Engine.willoughby_engine import Willoughby

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced_true(self):
        current_mileage = 60500
        last_service_mileage = 0
        engine=Willoughby(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_engine_should_be_serviced_false(self):
        current_mileage = 50000
        last_service_mileage = 0
        engine=Willoughby(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())