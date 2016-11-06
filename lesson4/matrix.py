matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix3 = []
print(len(matrix1[0]))

# i=1 j=0
def matrix_mult(matrix1,matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            for k in range(len(matrix2)):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
                return matrix3

matrix_mult(matrix1,matrix2)



