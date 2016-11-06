# release function range with yield
# check for (10)

def myrange(start,end,step=1):
    i = start
    if step == 0:
        raise StopIteration
    i = start
    if step > 0:
        while i<end:
            yield i
            i += step
    if step < 0:
        while i>end:
            yield i
            i += step
    if step == 1 and start>end:
        while i>end:
            yield i
            i -= step

for i in myrange(10):
  print(i)


