#TODO add bugs in this file
class Car:
    def __init__(self, VIN, make, model, year, hasExpiredTabs):
        self.VIN = VIN
        self.make = make
        self.model = model
        self.year = year
        self.hasExpiredTabs = hasExpiredTabs

    def getVIN(self):
        return self.VIN

    def setVIN(self, VIN):
        self.VIN = VIN

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def getHasExpiredTabs(self):
        return self.hasExpiredTabs

    def setHasExpiredTabs(self, hasExpiredTabs):
        self.hasExpiredTabs = hasExpiredTabs
