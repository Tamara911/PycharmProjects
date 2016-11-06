# route


array = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
        ]

def move_area(array,i,j):
    array[i][j]=2
    if(j+1<len(array[i]) and array[i][j+1] == 1):
        move_area(array,i,j+1)
    if(j-1 >=0 and array[i][j-1] == 1):
        move_area(array,i,j-1)
    if(i-1 >=0 and array[i-1][j] == 1):
        move_area(array,i-1,j)
    if(i+1 <len(array) and array[i+1][j] == 1):
        move_area(array,i+1,j)

def find_water(array):
    count = 0
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if(array[i][j] == 1):
                count+=1
                move_area(array,i,j)
    return count

print(find_water(array))