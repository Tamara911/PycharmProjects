# 1. fill stack
# 2. take value from stack

def factorial(n):
    if n>0:
        return factorial(n-1)*n
    else:
        return 1

def main():
    res = factorial(3)
    print(res)

main()

#