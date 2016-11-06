# home work

def f1(x):
    return x+1

def f2(x):
    return x*2

def generator(x):
    yield f1()
    yield f2()

f = generator(20)
res = next(f)
print(res)
res1 = next(f)
print(res1)
