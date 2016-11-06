def f(x):
    return x+1

def map(func,mylist):
    return [func(elem) for elem in mylist]

def main():
    lis = [1,2,3,4,5]
    new_lis = map(f,lis)
    print(new_lis)

main()
