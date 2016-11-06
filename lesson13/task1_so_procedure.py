# so - procedure
# 10 in i

def generator():
    print("Ok")
    i = yield 1
    print(i)
    print("Ok2")
    j = yield 2
    print(j)

f = generator()
k = next(f)
print(k)
k1 = f.send(10)
print("k1", k1)
k2 = f.send(20)
