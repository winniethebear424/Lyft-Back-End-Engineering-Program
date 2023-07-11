from abc import ABC, Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        
    def need_service(self):
        return self.engine.need_service() or self.battery.need_service()