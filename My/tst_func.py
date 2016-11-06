def divisors(integer):
    res = []
    i = 2
    while (i<integer):
        if integer%i == 0:
            res.append(i)
        i +=1
    if len(res) > 0:
        return res
    elif len(res) == 0:
        return (str(integer) + " is prime")

ff=divisors(11)
print(ff)


