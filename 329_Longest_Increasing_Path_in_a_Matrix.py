#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# DFS + Memoization

# Output 4
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

# Output 4
# matrix = [
#     [3, 4, 5],
#     [3, 2, 6],
#     [2, 2, 1]
# ]

# Output 1
# matrix = [
#     [1]
# ]

# Output 4
matrix = [
    [7, 7, 5],
    [2, 4, 6],
    [8, 2, 0]
]


def DFS(matrix, startNode, Cache, m, n):
    x, y = startNode
    Neighbors = [0, 0, 0, 0]

    # Up neighbor
    if x >= 1 and matrix[x-1][y] > matrix[x][y]:
        # Enter this if we already calculated that node, we don't have to
        # revisit the node again
        if Cache[x-1][y] != 0:
            Neighbors[0] = Cache[x-1][y]
        else:
            Neighbors[0] = DFS(matrix, (x-1, y), Cache, m, n)
    # Right neighbor
    if y < n-1 and matrix[x][y+1] > matrix[x][y]:
        # Enter this if we already calculated that node, we don't have to
        # revisit the node again
        if Cache[x][y+1] != 0:
            Neighbors[1] = Cache[x][y+1]
        else:
            Neighbors[1] = DFS(matrix, (x, y+1), Cache, m, n)
    # Down neighbor
    if x < m-1 and matrix[x+1][y] > matrix[x][y]:
        # Enter this if we already calculated that node, we don't have to
        # revisit the node again
        if Cache[x+1][y] != 0:
            Neighbors[2] = Cache[x+1][y]
        else:
            Neighbors[2] = DFS(matrix, (x+1, y), Cache, m, n)
    # Left neighbor
    if y >= 1 and matrix[x][y-1] > matrix[x][y]:
        # Enter this if we already calculated that node, we don't have to
        # revisit the node again
        if Cache[x][y-1] != 0:
            Neighbors[3] = Cache[x][y-1]
        else:
            Neighbors[3] = DFS(matrix, (x, y-1), Cache, m, n)

    # Plus one because this current node count as 1
    Cache[x][y] = max(Neighbors) + 1
    return Cache[x][y]


m = len(matrix)
n = len(matrix[0])
Cache = [[0 for _ in range(n)] for _ in range(m)]
for i, row in enumerate(matrix):
    for j, num in enumerate(row):
        if Cache[i][j] == 0:
            DFS(matrix, (i, j), Cache, m, n)
Max = 0
for row in Cache:
    for num in row:
        Max = max(Max, num)
print Max
