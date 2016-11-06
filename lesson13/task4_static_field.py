# static field - one for all methods in class
# better not to use
# common for all object in class

class A:
    count = 0

    def __init__(self,a,b):
        A.count += 1
        self.a=a
        self.b=b

    def f(self):
        return self.a+self.b

    @staticmethod
    def g(c,d):
        print(c+d+A.count)

def main():
    p = A(15,25)
    p1 = A(11,14)
    print(A.count)
    print(A.__dict__)
    A.count = 100
    print(A.count)
    A.g(10,20)

main()

