s = "dfgdf gf tdrth fdf"

def find_short(s):
    res = s.split(' ')
    res2 = []
    for i in range(len(res)):
        res2.append(len(res[i]))
    min2 = min(res2)
    return min2

ff = find_short("lets talk about javascript the best language")
print(ff)
