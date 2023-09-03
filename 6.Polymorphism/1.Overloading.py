class Shape:
    area = 0
    def area():
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        Shape.area = self.side ** 2
        return Shape.area
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        Shape.area = self.length * self.breadth
        return Shape.area
    
s1 = Square(4)
s2 = Rectangle(10, 5)
print(s1.area())
print(s2.area())