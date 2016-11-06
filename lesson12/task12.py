# генераторы и сопроцедуры

# генератор, если есть yield
#
def gen():
    print("Ok")
    yield 1
    print("Ok2")
    yield 2
    print("Ok3")

f = gen() # инициализируем тут гениратор
res = next(f)
print(res)
res1 = next(f)
print(res1)
res2 = next(f)