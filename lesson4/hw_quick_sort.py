def quick_sort(array):
    oporn_el = array[len(array) // 2]
    i = 0
    j = len(array) - 1
    while i <=j:
        while array[i] < oporn_el:
            i += 1
        while array[j] > oporn_el:
            j -= 1
        if i<= j:
            array[i], array[j] = array[j], array[i]
            i +=1
            j -=1
    if j > 0:
        array[:j+1] = quick_sort(array[:j+1])
    if i < len(array)-1:
        array[i-1:] =quick_sort(array[i-1:])
    return array

array = [7,8,97,1,3,7]
res = quick_sort(array)
print (res)

