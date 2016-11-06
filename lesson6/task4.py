import re

patern = re.compile("[\w]+([\w])+[y]$")
result = patern.match("aas354dfay")
if result == None:
    print("Doesn't match")
else:
    print("Ok")

print(result.group(1), result.group(0))


patern2 = re.compile()
result2 = patern2.match()
if result == None:
    print("Doesn't match")
else:
    print("Ok")

