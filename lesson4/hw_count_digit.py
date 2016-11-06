# Find a count of digits in a number by recursion

def len_number_recursion(s):
    count = 1
    if(s//10) == 0:
        return 1
    else:
        count += len_number_recursion(s // 10)
    return count

def main():
    s = 1234567890
    res = len_number_recursion(s)
    print(res)

main()
