# function range

def myrange(start,stop,step=1):
    i = start
    while (i<stop):
        yield i
        i +=step

for j in myrange(0,10,2):
    print(j)

f = myrange(0,5)
while True:
    try:
        j = next(f)
        print(j)
    except StopIteration:
        break
