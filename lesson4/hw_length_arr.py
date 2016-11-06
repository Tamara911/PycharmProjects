def len_arr(arr):
    if (arr!=[]):
        return (1 + (len_arr(arr[:-1])))
    else:
        return 0


arr = [1,5,2,7,3,5]

print(len_arr(arr))

