# polimorfizm - окружность ИМЕЕТ точку - аггрегация 

import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self,x,y,r):
        self.center=Point(x,y)

def distance(p1,p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

c1=Circle(10,20,30)
c2=Circle(20,30,40)

pp1 = Point(10,20)
pp2 = Point(20,30)

res = distance(c1,c2)
print(res)

res2 = distance(pp1,pp2)
print(res2)

e = 111