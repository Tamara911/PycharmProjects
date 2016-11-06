def f(y):
    x= 10
    def g():
        return x+y
    return g

res=f(7)
print(res())