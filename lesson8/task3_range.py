def myrange(start,end,step=1):
    i = start
    if step == 0:
        raise StopIteration
    i = start
    if step > 0:
        while i<end:
            yield i
            i += step
    else:
        while i>end:
            yield i
            i+= step

for i in myrange(5,0):
  print(i)

# for i in range(1,10,-1):
#     print(i)


