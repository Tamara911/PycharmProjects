# all

def odd_nambers(start,end):
    return [num for num in range(start,end) if(num%2 == 1)]

a = odd_nambers(5,10)
print(a)
