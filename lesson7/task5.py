def myfunc1(x):
    return x+1

def myfunc2(x):
    return x+2

myfuncdict = {"f1":myfunc1,"f2":myfunc2}
res = myfuncdict["f2"](100)+myfuncdict["f1"](200)
print(res)
