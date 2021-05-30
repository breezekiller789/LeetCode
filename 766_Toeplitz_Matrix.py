#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/toeplitz-matrix/

# EZ

# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]

# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
# matrix = [
#     [1, 2],
#     [2, 2]
# ]
m = len(matrix)
n = len(matrix[0])
for i, row in enumerate(matrix):
    for j, num in enumerate(row):
        if i+1 <= m-1 and j+1 <= n-1:
            if num != matrix[i+1][j+1]:
                print False
                exit()
print True
