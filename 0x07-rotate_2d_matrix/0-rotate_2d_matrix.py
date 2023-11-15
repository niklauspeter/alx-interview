#!/usr/bin/python3
"""
two D matrix provided as input
rotated 90 degrees clockwise
"""

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            offset += 1

# def arrRotation(A):
#     # A = [[1, 2, 3],
#     #      [4, 5, 6],
#     #      [7, 8, 9]]

#     Output = []
#     for i in range(len(A)):
#         row = []
#         for j in range(len(A[0])):
#             row.insert(i, A[i])
#         Output.append(row)
#     return Output
