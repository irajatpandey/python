# Abstract Class Method
from abc import ABC, abstractmethod 
class Bank(ABC): # can have both abstract and non abstract methods
    @abstractmethod
    def calculateRateOfInterest(self):
        pass
class SBI(Bank):
    def __init__(self, roi):
        self.__roi = roi
    
    def calculateRateOfInterest(self):
        return self.__roi * 12

class BOI(Bank):
    def __init__(self, roi):
        self.__roi = roi
    
    def calculateRateOfInterest(self):
        return self.__roi * 5
    

class HDFC(Bank):
    pass
s1 = SBI(7)
print(s1.calculateRateOfInterest())

s2 = BOI(8)
print(s2.calculateRateOfInterest())

#h1 = HDFC() #Can't instantiate abstract class HDFC with abstract method calculateRateOfInterest