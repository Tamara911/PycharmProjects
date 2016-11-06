def f1():
    print("a")
    yield 1
    print("b")
    yield 2
    print("c")
#    yield 3

for i in f1():
    print(i)

f = f1()
try:
    while True:
        i = next(f)
        print(i)
except StopIteration:
    print("Error")