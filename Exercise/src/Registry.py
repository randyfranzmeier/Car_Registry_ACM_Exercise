class Registry:
    def __init__(self, registry: list):
    self.registry = registry

    def add_car_to_registry(self, car):
        self.registry.append(car)

    def print_registered_cars(self):
        printf('Registered cars: ')
        for car of self.registry:
            print('Car: ' + car.model + ' ' + car.make)
            print('Year: ', car.year)
            print('Vin: ', car.VIN)
            print('Expired tabs? ', car.hasExpiredTabs)
            print('------------------------------------')

    def cars_have_expired_tabs(self):
        for car in self.registry:
            if not(car.hasExpiredTabs):
                return False
        return True