#!/usr/bin/env python3
def matrix_shape(matrix):

    mat = []
    while isinstance(matrix, list):
        mat.append(len(matrix))
        matrix = matrix[0]
    return mat


new_mat = [[1, 2, 4], [3, 4], [5, 6]]

print(matrix_shape(new_mat))  # Output: [2, 2]