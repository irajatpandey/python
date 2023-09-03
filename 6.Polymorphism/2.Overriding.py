class Car:
    numberOfGears = 0
    color = ""
    milage = -1
    price = -1

    def printDetails():
        print(numberOfGears)
        print(color)
        print(milage)
        print(price)

class Audi(Car):
    
    def __init__(self, numberOfGears, color, milage, price, selfOrAuto):
        self.__numberOfGears = numberOfGears
        self.__color = color
        self.__milage = milage
        self.__price = price
        self.__selfOrAuto = selfOrAuto 
        
    def printDetails(self):
        print(self.__numberOfGears)
        print(self.__color)
        print(self.__milage)
        print(self.__price)
        print(self.__selfOrAuto)   

a1 = Audi(6, "Black", 12, 9999999, "Auto")

a1.printDetails()
    
