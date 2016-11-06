# generator and so-procedure

def f1():
    print("a")
    yield 1
    print("b")
    yield 2
    print("c")
#    yield 3

f = f1()
res = next(f)
print(res)
res1 =next(f)
print(res1)
res2 = next(f)
print(res2)

