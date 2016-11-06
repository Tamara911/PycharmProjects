numbers = [23,5, 8, 12, 18, 22]

def sum_two_smallest_numbers(numbers):
    arr = []
    for i in range(0,len(numbers)):
        for j in range(1,len(numbers)):
            if i!=j:
                arr.append(numbers[i]+numbers[j])
    return min(arr)

ff = sum_two_smallest_numbers(numbers)
print(ff)
