import unittest

from Engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest):
    def test_engine_should_be_serviced_true(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_engine_should_be_serviced_false(self):
        current_mileage = 60000
        last_service_mileage = 40000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())