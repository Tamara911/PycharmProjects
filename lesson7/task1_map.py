# function higher order - v kachestve arg / znach - funkciu

# map applies function to list

def f(x):
    return x+1

def map(func,mylist):
    newlist = []
    for elem in mylist:
        new_elem = func(elem)
        newlist.append(new_elem)
    return newlist

def main():
    lis = [1,2,3,4]
    new_lis = map(f,lis)
    print(new_lis)

main()

