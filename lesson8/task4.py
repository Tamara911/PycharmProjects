# сопроцедурп
def f1():
    print("a")
    i = yield 80
    print("f1 "+str(i))
    j = yield 90
    print("f1 "+str(j))

f = f1()
res = next(f) # give 1
print(res)
res1 = f.send(10)
print(res1)
# res2 =f.send(100)
