# need parametr

def func_decorator(d):
    def external_wrapper(function):
        def wrapper(a,b):
            print("wrapper1")
            if (a>d):
                a = d
            res = function(a,b)
            return res
        return wrapper
    return external_wrapper


@func_decorator(11)
def func(a,b):
    return a+b

c = func(48,20)
print(c)