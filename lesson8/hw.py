def f1(x):
    return x+1

def f2(x):
    return x*2

def my_func_gen(*):
    for el in gen():
        yield el

gen = my_func_gen(f1,f2)
for func in gen:
    print(func(200))