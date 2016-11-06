# homework
def tester(list_of_tests):
    #print("first")
    def wrapper1(func):
        #print("IN FUNC")
        def wrapper2(arr1,word1):
            for i in range(0,len(list_of_tests)):
                arr = list_of_tests[i][0]
                word = list_of_tests[i][1]
                flag = func(arr,word)
                if flag!=list_of_tests[i][2]:
                    print("Failed")
            return func(arr1,word1)
        print("Test passed")
        return wrapper2
    return wrapper1

test_case = [
             (["cc","dd"],"ccdd",True)
            ,(["hh","gg"],"hhgg",True)
            ,(["aa","gaag"],"hhgg",False)
             ]

# for el in test_case:
#     print(el)
def concat(arr,word):
    if word == "":
        return True
    for i in range(1,len(word)+1):
        temp = word[0:i]
        if temp in arr and concat(arr, word[i:]):
            return True
    return False

@tester(test_case)
def wrapconcat(arr,word):
    return concat(arr,word)

arr = ["cc","dd","ahh","gg","ah"]
word = "ggahhahcc"
aa = wrapconcat(arr,word)
print(aa)





