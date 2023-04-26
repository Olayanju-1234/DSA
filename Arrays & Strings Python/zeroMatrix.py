# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def zeroMatrix(matrix):
    # check if matrix is empty
    if len(matrix) == 0:
        return "matrix is empty"

    # check if matrix is not a square matrix
    if len(matrix) != len(matrix[0]):
        return "matrix is not a square matrix"

    # check if there are any non-integers in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not isinstance(matrix[i][j], int):
                return "matrix contains non-integers"

    # check if there are any zeros in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                matrix[i][j] = "zero"

    # check if there are any zeros in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "zero":
                for k in range(len(matrix)):
                    matrix[i][k] = 0
                    matrix[k][j] = 0

    return matrix


print(zeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
print(zeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(zeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
print(zeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, "zero"]]))
