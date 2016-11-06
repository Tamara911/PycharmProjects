# function is named a part of code

# define a function and describe

def sum(start, end):
    result = start
    for i in range(start + 1, end + 1):
        result += i
    return result


r = sum(0, 3)
print(r)
