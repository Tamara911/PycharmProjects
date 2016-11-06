def f1(x):
    return x+1

def f2(x):
    return x*2

def mygenerator():
    print("a")
    func = yield 11
    k = yield 33
    print(func(k))
    func1 = yield 55
    print(func1(k))

f = mygenerator()
res = next(f)
print(res)
res1 = f.send(f1)
res1 = f.send(100)