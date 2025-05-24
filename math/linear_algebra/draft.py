#!/usr/bin/env python3

def add(arr1, arr2):

    if len(arr1) == len(arr2):
        return [arr1[i] + arr2[i] for i in range(len(arr1))]   

    else:
        return None
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add(arr1, arr2))
# print(arr1)
# print(arr2)
# # print(add(arr1, [1, 2, 3]))