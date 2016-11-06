# sort insert
arr = [2,5,1,7,0]

for i in range(1,len(arr)):
    while i>0 and arr[i]<arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -=1
        print(arr)

print(arr)

arr = [2,5,1,7,0,4,88,2]

# bubble sort
# mark of difficulties = O(n**2) - how compare and swap
n = 1
while n < len(arr):
    for i in range(len(arr)-n):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    n+=1

print(arr)



