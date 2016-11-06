# decorator with parameter
def mydecorator(start,end):
    def wrapper1(func):
        def wrapper2(x):
            if(x>start and x<end):
                return func(x)
            else:
                print("error")
        return wrapper2
    return wrapper1

@mydecorator(10,20)
def f(x):
    return x+1

res=f(16)
print(res)
