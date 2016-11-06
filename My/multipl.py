arr = [1, 2, 3]

def grow(arr):
    sum = 1
    for i in range(0,len(arr)):
        sum *=arr[i]
    return sum

ff = grow(arr)
print(ff)