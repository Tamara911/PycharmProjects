# sum of figures
import math

class Figure:
    def __init__(self):
        pass

    def get_square(self):
        pass

    def sum(self,other):
        return self.get_square() + other.get_square()

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def get_square(self):
        return self.side**2

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_square(self):
        return math.pi*self.radius**2

s = Square(4)
c = Circle(6)

print(s.sum(c))




