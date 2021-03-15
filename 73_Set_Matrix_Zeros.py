#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/set-matrix-zeroes/
# import time

# 1. 一個個檢查，一遇到零，就把該點的所有row都改成char，col也是
# 2. 改的同時，要注意，萬一遇到零的話，不要去改到那個零，跳過去，把零留著
# 3. 整張改完之後，再掃一次，把char都改成0


def Explode(row, col):
    matrix[row][col] = 'a'
    # 列先爆（爆裂SR)
    for i in range(n):
        if matrix[row][i] != 0:
            matrix[row][i] = 'a'
        else:
            continue
    # 行爆
    for i in range(m):
        if matrix[i][col] != 0:
            matrix[i][col] = 'a'
        else:
            continue


matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
# matrix = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]

m, n = len(matrix), len(matrix[0])
for row in range(m):
    for col in range(n):
        # print row, col, matrix[row][col]
        if matrix[row][col] == 0:
            Explode(row, col)

for row, i in enumerate(matrix):
    for col, j in enumerate(i):
        if j == 'a':
            matrix[row][col] = 0
for i in matrix:
    print i
