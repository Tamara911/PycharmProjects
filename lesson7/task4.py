def func():
    def inner_func():
        print("Inner_func 2")
    return inner_func

a = func()
#print(a)
a() # this is call of function


