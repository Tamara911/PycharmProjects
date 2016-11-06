# Bubble sort using recursion

def recursion_bubble(arr):
    n = len(arr)
    while n>0:
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        n -=1
        recursion_bubble(arr[0:n-1:])
    return arr

arr = [20,7,0,11,77,3,8]
res = recursion_bubble(arr)
print(res)