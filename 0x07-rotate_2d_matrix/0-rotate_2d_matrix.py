#!/usr/bin/python3
"2D Matrix rotation"


def rotate_2d_matrix(matrix):
    "rotation"
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
