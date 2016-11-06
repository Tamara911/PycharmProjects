# bashni Hanoy
# n - disc
# a,b,c - sterzhni
count = 0

def hanoy(n,a,b,c):

    if n > 0:
        global count
        count+=1
        hanoy(n-1,a,c,b)
        print("disk " + str(n) + " from " + a + " to " + c)
        hanoy(n-1,b,a,c)

hanoy(4,"A","B","C")
print(count)