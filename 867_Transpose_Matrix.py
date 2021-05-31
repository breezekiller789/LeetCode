#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/transpose-matrix/

# Output: [[1,4,7],[2,5,8],[3,6,9]]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Output: [[1,4],[2,5],[3,6]]
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

m = len(matrix)
n = len(matrix[0])
result = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    for j in range(n):
        result[j][i] = matrix[i][j]
print result
