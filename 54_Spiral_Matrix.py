#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/spiral-matrix/
# import time


def Right(x, y):
    shift = 0
    for shift in range(n-y):
        if matrix[x][y+shift] not in visited:
            visited.append(matrix[x][y+shift])
        else:
            # 因為遇到不是的之後要往回推一步
            return [x, y+shift-1]
    return [x, y+shift]


def Down(x, y):
    shift = 0
    for shift in range(m-x):
        if matrix[x+shift][y] not in visited:
            visited.append(matrix[x+shift][y])
        else:
            return [x+shift-1, y]
    return [x+shift, y]


def Left(x, y):
    shift = 0
    for shift in range(n-y+cnt):
        if matrix[x][y-shift] not in visited:
            visited.append(matrix[x][y-shift])
        else:
            # 因為遇到不是的之後要往回推一步
            return [x, y-shift+1]
    return [x, y-shift]


def Up(x, y):
    shift = 0
    for shift in range(m-x+cnt):
        if matrix[x-shift][y] not in visited:
            visited.append(matrix[x-shift][y])
        else:
            return [x-shift+1, y]
    return [x-shift, y]


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
# matrix = [
#     [1]
# ]
# matrix = [
#     [1],
#     [2],
#     [3],
#     [4],
#     [5]
# ]
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8],
#     [9, 10],
#     [11, 12]
# ]
# matrix = [
#     [1, 2, 3, 4, 5, 6],
#     [7, 8, 9, 10, 11, 12],
#     [13, 14, 15, 16, 17, 18],
#     [19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30]]
matrix = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13],
    [14, 15, 16]]

m = len(matrix)
n = len(matrix[0])
cnt = n-3

ref = [x for i in matrix for x in i]
visited = []
x_position, y_position = 0, 0
while set(visited) != set(ref):
    # todo : 回傳的位置要移動，為下一個準備
    x_position, y_position = Right(x_position, y_position)
    x_position += 1
    if x_position >= m or y_position >= n:
        break
    # print x_position, y_position
    x_position, y_position = Down(x_position, y_position)
    y_position -= 1
    # print x_position, y_position
    x_position, y_position = Left(x_position, y_position)
    x_position -= 1
    # print x_position, y_position
    x_position, y_position = Up(x_position, y_position)
    y_position += 1
    # cnt += 1
    print visited
    # time.sleep(1)
    # print x_position, y_position
print visited
