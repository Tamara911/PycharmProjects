# func

s=234567

def len_number(a):
    count=1
    b = a//10
    while(b!=0):
        count+=1
        b=b//10
    return count

def main():
    a = 2356
    res = len_number(a)
    print(res)

main()

