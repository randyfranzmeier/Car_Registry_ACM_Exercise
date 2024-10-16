from Solution.src.Car import Car
class Registry:
    def __init__(self, registry: list):
        self.registry = registry

    def getRegistry(self):
        return self.registry

    def addCarToRegistry(self, car):
        self.registry.append(car)

    def setRegistry(self, registry: list):
        self.registry = registry

    def printRegisteredCars(self):
        print('Registered cars: ')
        for car in self.registry:
            print('Car: ' + car.make + ' ' + car.model)
            print('Year: ', car.year)
            print('Vin: ', car.VIN)
            print('Expired tabs? ', car.hasExpiredTabs)
            print('------------------------------------')

    def carsHaveExpiredTabs(self):
        for car in self.registry:
            if car.hasExpiredTabs:
                return True
        return False