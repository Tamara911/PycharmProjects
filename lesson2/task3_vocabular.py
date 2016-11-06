# empty dictionary
myDict = {}

myDict = {"aaa": ["ddd", 10], "bbb": 90, 80: "uuuu", 70: 100}

# first is key, second is value

print(myDict["aaa"])
# dictionary can be changed

myDict["kkk"] = "odpfg"
print(myDict["kkk"])

# if we don't have el
print(myDict.get("aaa", "no elem"))

# all keys
print(myDict.keys())
print(myDict.values())

for key, value in myDict.items():
    print(key)
    print(value)

# items gives spysoc of cortage