from Solution.src.Car import Car


class User:

    def getUserCarOptions(self):
        vin = self.getUserVin()
        make = self.getUserMake()
        model = self.getUserModel()
        year = self.getUserYear()
        hasExpiredTabs = self.getUserBoolInput('Does your car have expired tabs (yes-> y, no -> n): ')
        return Car(vin, make, model, year, hasExpiredTabs)

    def getUserVin(self):
        while True:
            vin = input('Please enter your cars VIN \nA VIN is a sequence of 5 letters and 5 numbers: ')
            if self.isValidVin(vin):
                return vin
            else:
                print('Invalid input. Try again.')

    def getUserMake(self):
        while True:
            make = input('Please enter your cars make (eg. Honda): ')
            if self.isValidMakeOrModel(make, True):
                return make
            else:
                print('invalid input. Try again.')

    def getUserModel(self):
        while True:
            model = input('Please enter your cars model (eg. Civic): ')
            if self.isValidMakeOrModel(model, False):
                return model
            else:
                print('invalid input. Try again.')

    def getUserYear(self):
        while True:
            try:
                year = int(input('Please enter your cars year: '))
                if year > 2025 or year < 1900:
                    print('invalid year. Please enter a year from 1901-2025')
                else:
                    return year
            except:
                print("Invalid input. Please try again.")

    def getUserBoolInput(self, prompt):
        while True:
                expiredTabs = input(prompt).lower()
                if len(expiredTabs) == 1:
                    if expiredTabs == 'y':
                        return True
                    elif expiredTabs == 'n':
                        return False
                print("Invalid input. Please try again.")

#VIN must have 5 digits and 5 letters
    def isValidVin(self, VIN):
        if len(VIN) == 0:
            return False

        letters, numbers = 0, 0
        for char in VIN:
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                numbers += 1
            else:
                return False #invalid
        return letters == 5 and numbers == 5

    def isValidMakeOrModel(self, input, isMake):
        for char in input:
            if not (char.isalpha()) and isMake:
                return False
        return True


