# reduce
# return number

ll = [1,2,3]

def ff(x):
    return x+1

def map(f,l):
    return [f(el) for el in l]

res = map(ff,ll)
print(res)

def reduce(f,l,init):
    res = init
    for el in l:
        res=f(res,el)
    return res

def sum(a,b):
    return a*b

res = reduce(sum,res,1)
res2 = reduce(sum,map(ff,ll),1)
print(res)
print(res2)