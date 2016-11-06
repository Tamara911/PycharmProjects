# how to distribute memory for List

def f(a):
    a[1]=100
    return

def main():
    mas = [11,2,3,4]
    f(mas)
    print(mas)
    print(mas[1])

main()
