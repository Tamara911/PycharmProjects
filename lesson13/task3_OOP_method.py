class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def f(self):
        return self.a+self.b

class noname:
    @staticmethod
    def main():
        p = A(15,25)
        print(p.f())

noname.main()

# staticmethod means that method is static