#TODO add bugs in this file
from Exercise.src.Registry import Registry
from Exercise.src.User import User


class Main:

    def startProgram(self):
        registry = Registry([])
        user = User()
        self.printWelcomeMessage()

        while True:
            car = user.getUserCarOptions()
            registry.addCarToRegistry(car)
            registry.printRegisteredCars()
            if not(user.getUserBoolInput('Register more cars? (yes -> y, no -> n): ')):
                break

        print('Thanks for registering your cool cars!')
        if registry.carsHaveExpiredTabs():
            print('Make sure to renew your tabs!')


    def printWelcomeMessage(self):
        print('-----Welcome to Cool Car Registry-----')
        print('You will be prompted to enter your cars information, and can register multiple cars if you wish.')
        print('Business hours are 4:30-6:30pm Every Thursday.\n')



app = Main()
app.startProgram()

