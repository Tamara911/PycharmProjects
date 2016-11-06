# global variable, static field - don't use!
a = 10

def f():
    global a # doesn't create new a, use a = 10
    a = 30
    return

def main():
    print(a)
    f()
    print(a)

main()
