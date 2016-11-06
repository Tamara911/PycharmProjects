import math

class Quadrangle:
    def __init__(self, side1, side2, side3, angle1, angle2):
        self.side1=side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2

class Parallelogram(Quadrangle):
    def __init__(self, side1,side2,angle):
        Quadrangle.__init__(self, side1, side2, side1, angle, 180-angle)

class Rectangle(Parallelogram):
    def __init__(self,side1,side2):
        Parallelogram.__init__(self,side1,side2, 90)


