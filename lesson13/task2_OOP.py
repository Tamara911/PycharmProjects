# class as type of data
# a, b are fields of class or atributes
# init - method

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def main():
    # p = A(10,20)
    # print(p.a)
    # print(p.b)
    p = A.__new__(A)
    A.__init__(p,10,20)
    print(p.a)
    print(p.b)
    p1 = A(30,40)
    print(p.a, p1.a)
    print(p.__dict__['a']) # p.a

main()
