readMe = open('aaa.html','r').read()

b = list(readMe)
print(b)

symbol1=b[0]
symbol2=b[5]

print(symbol1, symbol2)

count = 0
count2 = 0
str1 = [0]

for i,j in range(1, len(b)):
    if (b[i] == symbol1):
        start = i
        if(b[j] == symbol2):
            end = j
    # str1[i]=b[(i+1):b[j]]
    # print(str1[i])
        print(b[i+1:j])
# 1) split </
# 2) split >









# print(count, count2 )



