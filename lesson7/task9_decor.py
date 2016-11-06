# decorator of function
def mydecorator(func):
    def mywrapper(x):
        print("wrapper")
        return func(x)
    return mywrapper

@mydecorator
def f(x):
    return x+1

# res = f(10)
myfunc=mydecorator(f)
res=myfunc(100)
print(res)

