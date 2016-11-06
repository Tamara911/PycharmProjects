# Task: If worrd consists from array elements 
arr = ["aa", "aab", "gc", "cc"]
word = "gaac"

def concat(arr):
    word3 = ""
    for j in range(0,len(arr)):
        word3 = word3 + arr[j]
    return word3

def sortByLength(input):
    return len(input)

def if_exist (arr, word):
    word2 = []
    arr.sort(key=sortByLength, reverse=True)
    for i in range(0, len(arr)):
        word2 = word.split(arr[i])
        print(word2)
        word = concat(word2)
        print(word)
    if (len(word) > 0):
        print("Word doesn't consist from array")
    else:
        print("Word consists from array")

if_exist(arr, word)
