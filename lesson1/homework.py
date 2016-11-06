# find min element
mas=[2,4,3,5,8,1,7]

min=mas[0]
min_ind=0

for i in range(len(mas)-1):
    if mas[i+1]<min:
        min=mas[i+1]
        min_ind=i+1

print("min element is equel "+str(min))
print("min index is equel "+str(min_ind))

# find max element
max=mas[0]
max_ind=0

for j in range(len(mas)-1):
    if mas[j]>max:
        max=mas[j]
        max_ind=j

print("max element is equel "+str(max))
print("max index is equel "+str(max_ind))