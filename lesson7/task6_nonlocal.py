# global and nonlocal
a = 100

def f1():
    a = 200
    def f2():
        nonlocal a # higher on 1 level
        a = 400
    f2()
    print(a)

f1()
print(a)