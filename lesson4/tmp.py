from random import randint


def main():
    size = int(input('Input matrix size (integer): '))
    end_range = int(input('Input integer end range for matrix meaning randomization staring from 1 to: '))
    matrix1 = rand_matrix(1, end_range, size)
    matrix2 = rand_matrix(1, end_range, size)
    print("First random filed matrix")
    output(matrix1)
    print("Second random filed matrix")
    output(matrix2)
    print("Result of matrix multiplication")
    output(matrix_mul(matrix1, matrix2, size))


# function matrix_mul for multiplication two int symmetric matrix

def matrix_mul(input_matrix1, input_matrix2, matrix_size):
    end_matrix = rand_matrix(0, 0, matrix_size)
    if len(input_matrix1) != len(input_matrix2):
        print("matrix can't be multiplied")
    else:
        size = len(input_matrix1)
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    end_matrix[i][j] += input_matrix1[i][k] * input_matrix2[k][j]

    return end_matrix


# function rand_matrix for generating random int matrix
# range_start - start range int
# range_end - end range int
# size - matrix size

def rand_matrix(range_start, range_end, size):
    mat_rand = [[randint(range_start, range_end) for j in range(size)] for i in range(size)]
    return mat_rand


def output(matrix):
    for r in matrix:
        print(r)


main()