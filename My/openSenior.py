def openOrSenior(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] >= [55,7]:
                return "Senior"
            else:
                return "Open"

data = [[55,7],[34,5]]
ff = openOrSenior(data)
print(ff)
print(data[0][1])
print(len(data))

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
