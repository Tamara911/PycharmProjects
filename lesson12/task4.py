# ф-ия высшего порядка: это ф-ия которая возвращает ф-ию или принимает в качестве аргумента другю ф-ию

# map returns list

def map(f,l):
    res=[]
    for el in l:
        res.append(f(el))
    return res

def ff(x):
    return x+1

ll = [10,20,30]

res = map(ff,ll)
print(res)

# second version
def map(f,l):
    return [f(el) for el in l]

res = map(ff,ll)
print(res)