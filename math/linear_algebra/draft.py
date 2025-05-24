#!/usr/bin/env python3

def add(arr1, arr2):

    if len(arr1) == len(arr2) and  len(arr1[0]) == len(arr2[0]):
        return [[arr1[i][j] + arr2[i][j] for i in range(len(arr1[0]))]
        for j in range(len(arr1))
        ]


    else:
        return None


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add(mat1, mat2))
print(mat1)
print(mat2)
print(add(mat1, [[1, 2, 3], [4, 5, 6]]))