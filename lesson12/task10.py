# need check then decorator

def func_decorator(function):
    def wrapper(a,b):
        print("wrapper1")
        if (a>20):
            a = 20
        res = function(a,b)
        return res
    return wrapper


@func_decorator
def func(a,b):
    return a+b

c = func(48,20)
print(c)