#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/number-of-islands/

# 這題參考200題的number of island，寫過的東西，BFS來做就好了。

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]


# ============Code Starts============
m = len(grid)
n = len(grid[0])


def Has_Surrounding_1(x, y):
    ret = []
    if x-1 >= 0:
        if grid[x-1][y] == 1:
            ret.append([x-1, y])
    if y+1 < n:
        if grid[x][y+1] == 1:
            ret.append([x, y+1])
    if y-1 >= 0:
        if grid[x][y-1] == 1:
            ret.append([x, y-1])
    if x+1 < m:
        if grid[x+1][y] == 1:
            ret.append([x+1, y])
    return ret


def BFS(x, y):
    Q = []
    Q.append([x, y])
    Area = 0
    while Q:
        Area += 1
        x, y = Q.pop()
        positions = Has_Surrounding_1(x, y)
        for i in positions:
            if i not in Q:
                Q.append(i)
        # Q.extend(positions)
        grid[x][y] = 0
    return Area


island = 0
Max_Area = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            Area = BFS(i, j)
            if Area > Max_Area:
                Max_Area = Area
            island += 1
print Max_Area
