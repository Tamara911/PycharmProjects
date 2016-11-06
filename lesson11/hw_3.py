# NSD

# if a and b are not odd then a,b divide on 2
# if a is odd then (a, b div 2)
# if a and b are odd numbers (a,b-a div 2)

def fuctor_nsd(a,b):
    if a%2 == 0 and b%2 == 0:
        return fuctor_nsd(a>>1,b>>1)

    if a % 2 != 0 and b%2 == 0:
        return b>>1

    if a % 2 == 0 and b % 2 != 0:
        return a>>1

    if a % 2 != 0 and b % 2 != 0:
        if a>b:
            return (b-a)>>1
        else:
            return (a-b)>>1

a = 10
b=a<<1
print(b)
