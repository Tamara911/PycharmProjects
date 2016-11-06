# sort vyborom / choice

arrayToSort=["as","abs","der","bbb"]

def choice_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

print(choice_sort(arrayToSort))

arrayToSort= [2, 6, 9, 3, 1, 7]
# sort vstavka / insert
def insert_sort(arrayToSort):
    a=arrayToSort
    for i in range(len(a)):
        v=a[i]
        j=i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j-1
        a[j] = v
#        print a
    return a

print(insert_sort(arrayToSort))

arrayToSort = [3,2,1]
# puzyrok / bubble
def bubble_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a),0,-1):
        for j in range(1,i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
                print(a)
    return a

print(bubble_sort(arrayToSort))

