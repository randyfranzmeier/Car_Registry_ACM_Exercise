from Solution.src.Car import Car
class Registry:
    def __init__(self, registry: list):
        self.registry = registry

    def add_car_to_registry(self, car):
        self.registry.append(car)

    def print_registered_cars(self):
        print('Registered cars: ')
        for car in self.registry:
            print('Car: ' + car.make + ' ' + car.model)
            print('Year: ', car.year)
            print('Vin: ', car.VIN)
            print('Expired tabs? ', car.hasExpiredTabs)
            print('------------------------------------')

    def cars_have_expired_tabs(self):
        for car in self.registry:
            if car.hasExpiredTabs:
                return True
        return False