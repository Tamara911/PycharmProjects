# lyamda function

def map(func,mylist):
    return [func(elem) for elem in mylist]

new_list=map(lambda x:x+1 if(x>0) else x+3, [1,2,-3])
print(new_list)

