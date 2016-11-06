# while
sum=0
i=1
while (i <= 5):
    sum=sum+i
    i+=1
print(sum)

fact=1
sum=0
for i in range(0,6):
    sum=sum+10**i/fact
    fact=fact*(i+1)

print(sum)

temp=1
sum=temp
for j in range(1,11):
    temp=(10/j)*temp
    sum=sum+temp

print(sum)


