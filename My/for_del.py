data = [[16, 23],[73,1],[56, 20],[1, -1]]
n = []
def openOrSenior(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][0]>=55 and data[j][1]>=7:
                print(str(data[i][0]) + " 1")
                print(str(data[j][1]) + " 2")
                n.append("Senior")
            else:
                print(str(data[i][0]) + " 3")
                print(str(data[j][1]) + " 4")
                n.append("Open")
        return n

ff = openOrSenior(data)
print(ff)


