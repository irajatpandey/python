# Fraction class 

class Fraction:
    def __init__(self, num = 0, den = 1):
        self.num = num
        self.den = den 
    def printFraction(self):
        print(self.num, "/", self.den)

f1 = Fraction(2, 3)
f1.printFraction() # 2/3
f2 = Fraction()
f2.printFraction() # 0/1

f3 = Fraction(1)
f3.printFraction() # 1/1