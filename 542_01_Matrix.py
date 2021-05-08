#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/01-matrix/


def UpdateNeighbors(mat, x, y, Rows, Cols, Visited, Q):
    # Up neighbor
    if x >= 1 and y < Cols and (x-1, y) not in Visited:
        Q.append((x-1, y))
        Visited.add((x-1, y))
    # Right neighbor
    if x < Rows and y < Cols-1 and (x, y+1) not in Visited:
        Q.append((x, y+1))
        Visited.add((x, y+1))
    # Down neighbor
    if x < Rows-1 and y < Cols and (x+1, y) not in Visited:
        Q.append((x+1, y))
        Visited.add((x+1, y))
    # Left neighbor
    if x < Rows and y >= 1 and (x, y-1) not in Visited:
        Q.append((x, y-1))
        Visited.add((x, y-1))


def BFS(mat, x, y, Rows, Cols):
    start = (x, y)
    Q = [start]
    Visited = {start}
    Dist = 0
    while Q:
        Count = len(Q)
        while Count > 0:
            current_X, current_Y = Q.pop(0)
            if mat[current_X][current_Y] == 0:
                return Dist
            UpdateNeighbors(mat, current_X, current_Y, Rows, Cols, Visited, Q)
            Count -= 1
        Dist += 1


mat = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

Rows = len(mat)
Cols = len(mat[0])

for idx, row in enumerate(mat):
    for jdx, col in enumerate(row):
        if col == 1:
            mat[idx][jdx] = BFS(mat, idx, jdx, Rows, Cols)
print mat
