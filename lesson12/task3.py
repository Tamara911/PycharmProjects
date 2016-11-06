# nonlocal

def f():
    a = 30
    def g():
        a = 40 # оценила, как создание новой переменной
    print(a)
    g()
    print(a)

f()

# если хотим изменить а, а не создавать новое - then use nonlocal

def f():
    a = 30
    def g():
        nonlocal a
        a = 40 # оценила, как создание новой переменной
    print(a)
    g()
    print(a)

f()