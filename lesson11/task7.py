# recursion

def fuctorial(n):
    if n>0:
        return n*fuctorial(n-1)
    else:
        return 1

def main():
    res=fuctorial(3)
    print(res)

main()