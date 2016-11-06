a = 10

def f():
    global a # записать в а 3, а не создавать новую переменнуюы
    a = 3


print(a)
f()
print(a)