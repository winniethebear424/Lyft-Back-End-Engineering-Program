from Engine import engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.willoughby_need_service = 60000

    def engine_should_be_serviced(self):
        
        return self.current_mileage - self.last_service_mileage > self.willoughby_need_service
