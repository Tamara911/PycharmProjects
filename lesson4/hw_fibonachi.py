# Find Fibonachi function with the next conditions:
# f(n) = f(n-1) + f(n-2)
# f(0) = 1
# f(1) = 1

def fibonachi(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1:
        return fibonachi(n-1) + fibonachi(n-2)
    else:
        return 0

def main():
    res = fibonachi(4)
    print(res)

main()

