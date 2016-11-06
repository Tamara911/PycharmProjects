a = 12

if isinstance(a, int) == True:
    print("Ok")
else:
    False


b = 2
c = 20

d = c&(b-1) # остаток от деления с на b
print(d)

e = (~a & 1)
print(e)

f = (a & 1) # =0 когда чётное 
print(f)

