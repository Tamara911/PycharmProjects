# decorator
# это тоже ф-ия, которая оболочка для другой ф-иию Сначало оболочка, потом ф-ия

def func_decorator(function):
    def wrapper(a,b):
        print("wrapper1")
        res = function(a,b)
        return res
    return wrapper


@func_decorator
def func(a,b):
    return a+b

c = func(10,20)
print(c)
