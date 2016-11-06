arr = ["aa", "aab", "gc", "cc"]
word = "aab"

def concat(arr,word):
    if word == "":
        return True
    for i in range(1,len(word)+1):
        temp = word[0:i]
        if temp in arr and concat(arr, word[i:]):
            return True
    return False

print(concat(arr, word))

# i = 3
# print(word[0:i])
# print(word[i:])
# ctrl + /

