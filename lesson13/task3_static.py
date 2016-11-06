# staticmethod don't need self, don't need create object

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def f(self):
        return self.a+self.b

    @staticmethod
    def g():
        print("Static")

    @staticmethod
    def gg(e,d):
        print(e+d)

def main():
    p = A(15,25)
    print(p.f())
    A.g()
    A.gg(11,14)
    print(A.__dict__)
    print(p.__dict__)
    p.c = 300 # add 300 to dictionary of object p
    print(p.c)
    d = p.f() # the same as d1 = A.f(p)
    d1 = A.f(p)
    d2 = A.__dict__['f'].__call__(p)
    print(d,d1,d2)


main()

