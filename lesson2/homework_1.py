# exists word and list

str1 = ["aa", "bb", "cc"]
str2 = "ccaabbccaa"

count=0
for i in range(0,len(str2),2):
    for j in range(0,len(str1)):
        if (str2[i:i+2]) in (str1[j]):
            count+=1
            print(count)
        else:
            count+=0

if (count == len(str2)/2):
    print("Word is correct")
else:
    print("Word is incorrect")

# task 2
c = 10
d = 1
d = d <<1
d = ~ d
print(bin(d))
