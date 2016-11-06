# Find an order of digit in a number
def len_number(s):
    count = 1
    b = s // 10
    while (b != 0):
        count += 1
        b = b // 10
    return count

def main3():
    s = 10375
    res = len_number(s)
    print(res)

def find_number(s, symb):
    res = 0
    length = len_number(s)
    how_divide = length - symb - 1
    for i in range(1, how_divide + 1):
        s = s // 10
    res = s - (s // 10) * 10
    return res

result_final = find_number(1234567890, 5)
print(result_final)



