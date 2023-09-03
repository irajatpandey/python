# class and objects

class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def printCarDetails(self):
        print("Car name is ", self.name)
        print("Car color is ", self.color)
        print("Car's price is ", self.price)
        print(id(self)) #output - 1830331738832

c1 = Car("BMW", "Black", 45000)
c1.printCarDetails()
print(id(c1)) # output - 1830331738832



#print(type(c1))


# print(c1.name)
# print(c1.color)
# print(c1.price)


