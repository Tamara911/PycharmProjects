# merge sort using recursion

def merge(array):
    if len(array) > 2:
        mid =len(array)//2
        print(mid)
        first_arr = merge(array[0:mid])
        print("first_arr ", first_arr)
        second_arr = merge(array[mid:])
        print("second_arr ", second_arr)
        result_arr = []
        i = 0
        j = 0
        while i < len(first_arr) and j < len(second_arr):
            if first_arr[i] < second_arr[j]:
                result_arr.append(first_arr[i])
                i += 1
                print("result_arr i", result_arr)
            else:
                result_arr.append(second_arr[j])
                j += 1
                print("result_arr j", result_arr)
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

#array = []
#string_input = input()
#string_input_array = string_input.split(",")
#for i in range(0,len(string_input_array)):
#  array.append(int(string_input_array[i]))

array = [10,30,29,6,55,3,8,5]

aa = (merge(array))
print(aa)