# merge sort using recursion + decorator
def test_merge(test_case):
    def wrapper1(func):
        def wrapper2(array):
            for i in range(0,len(test_case)):
                arr = test_case[i][0]
                sort_array = test_case[i][1]
                flag = func(sort_array)
                if flag!=test_case[i][2]:
                    print("Failed")
            return func(array)
        print("Test passed")
        return wrapper2
    return wrapper1

test_case = [
             ([2,5,1,6],[1,2,5,6],True)
            ,([2,5,1,6],[2,5,1,6],False)
             ]

@test_merge
def wrapper_merge(array):
    merge(array)

def merge(array):
    if len(array) > 2:
        mid =len(array)//2
        first_arr = merge(array[0:mid])
        second_arr = merge(array[mid:])
        result_arr = []
        i = 0
        j = 0
        while i < len(first_arr) and j < len(second_arr):
            if first_arr[i] < second_arr[j]:
                result_arr.append(first_arr[i])
                i += 1
            else:
                result_arr.append(second_arr[j])
                j += 1
        if i < len(first_arr):
            result_arr += first_arr[i:]
        if j < len(second_arr):
            result_arr += second_arr[j:]
        return result_arr
    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    if len(array) < 2:
        return array

array = [10,30,29,6,55,3,8,5]

@test_merge(test_case)
def wrapconcat(array):
    return merge(array)

aa = wrapconcat(array)
print(aa)
