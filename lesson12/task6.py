# ф-ия котор возвращ другую ф-ию

def f():
    def g(x):
        return x+1
    return g

ff = f()
print(ff) # return adress
print(ff(10)) # return function
print(ff.__call__(10))
