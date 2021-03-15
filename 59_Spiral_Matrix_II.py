#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/spiral-matrix-ii/
# import time


def Right(x, y):
    shift = 0
    for shift in range(n-y):
        # 如果該點值是零，代表還沒拜訪過，就pop一個值放進去
        if matrix[x][y+shift] == 0:
            matrix[x][y+shift] = ref.pop()
        else:
            # 因為遇到不是的之後要往回推一步
            return [x, y+shift-1]
    return [x, y+shift]


def Down(x, y):
    shift = 0
    for shift in range(m-x):
        # 如果該點值是零，代表還沒拜訪過，就pop一個值放進去
        if matrix[x+shift][y] == 0:
            matrix[x+shift][y] = ref.pop()
        else:
            # 因為遇到不是的之後要往回推一步
            return [x+shift-1, y]
    return [x+shift, y]


def Left(x, y):
    shift = 0
    for shift in range(y+1):
        # 如果該點值是零，代表還沒拜訪過，就pop一個值放進去
        if matrix[x][y-shift] == 0:
            matrix[x][y-shift] = ref.pop()
        else:
            # 因為遇到不是的之後要往回推一步
            return [x, y-shift+1]
    return [x, y-shift]


def Up(x, y):
    shift = 0
    for shift in range(x):
        # 如果該點值是零，代表還沒拜訪過，就pop一個值放進去
        if matrix[x-shift][y] == 0:
            matrix[x-shift][y] = ref.pop()
        else:
            # 因為遇到不是的之後要往回推一步
            return [x-shift+1, y]
    return [x-shift, y]


# 各種測資
n = 4
m = n
matrix = [[0 for x in range(n)] for i in range(n)]  # 初始化我就都先放零
ref = [x for x in xrange(n*n, 0, -1)]   # 倒著放，這樣就用pop來拿值就好
# [
#     [1,2,3],
#     [8,9,4],
#     [7,6,5]
# ]
# [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
# ]

x_position, y_position = 0, 0

# 如果還有值沒有被拿，代表還沒有全部拜訪完。
while ref:
    # 回傳的位置要移動，為下一個準備，往右走到底之後，下一步是往下走，x座標+1
    x_position, y_position = Right(x_position, y_position)
    x_position += 1

    # 往下走完之後y座標往左移一格
    x_position, y_position = Down(x_position, y_position)
    y_position -= 1

    # 往左走完之後x座標往上一格
    x_position, y_position = Left(x_position, y_position)
    x_position -= 1

    # 往上走完之後y座標往右一格
    x_position, y_position = Up(x_position, y_position)
    y_position += 1

print matrix
