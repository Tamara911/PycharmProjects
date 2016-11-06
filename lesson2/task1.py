# exist function

str1= '[[[   ]]]'
str2="aaa"

symbol=str1[0]
count=1

for i in range(1,len(str1)):
    if(str1[i]==symbol):
        count+=1
    else:
        break

part_of_res1=str1[0:count]
part_of_res2=str1[-1:-1-count:-1]

result=part_of_res1+str2+part_of_res2
print(result)
