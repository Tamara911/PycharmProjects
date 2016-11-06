# nasledovanie
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt(((self.x-self.other)**2)+((self.y-self.other)**2))

class Circle(Point):
    def __init__(self,x,y,r):
        Point.__init__(self,x,y) # nasledovanie
    #    super(Circle,self).__init__(x,y) # analog predyduschemu
        self.r = r

c = Circle(10,20,30)
print(c.x)
print(c.__dict__)
