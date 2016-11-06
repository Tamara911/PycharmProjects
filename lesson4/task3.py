# max el in array

# max in n-1 and compare n with this

def max_el(array,start,last):
    if(last>start):
        m = max_el(array, start, last-1)
        if(m>array[last]):
            return m
        else:
            return array[last]
    if(last == start):
        return array[last]
    if(last<start):
        return None

a=[10,40,500,20,2,6]

res = max_el(a,0,2)
print(res)
