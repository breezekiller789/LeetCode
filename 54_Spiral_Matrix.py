#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/spiral-matrix/
# import time


def Right(x, y):
    shift = 0
    for shift in range(n-y):
        # 如果目前這個格子還沒拜訪過，就把它加進拜訪名單裡頭
        if matrix[x][y+shift] not in visited:
            visited.append(matrix[x][y+shift])
        else:
            # 因為遇到不是的之後要往回推一步
            return [x, y+shift-1]
    return [x, y+shift]


def Down(x, y):
    shift = 0
    for shift in range(m-x):
        # 如果目前這個格子還沒拜訪過，就把它加進拜訪名單裡頭
        if matrix[x+shift][y] not in visited:
            visited.append(matrix[x+shift][y])
        else:
            # 因為遇到不是的之後要往回推一步
            return [x+shift-1, y]
    return [x+shift, y]


def Left(x, y):
    shift = 0
    for shift in range(y+1):
        # 如果目前這個格子還沒拜訪過，就把它加進拜訪名單裡頭
        if matrix[x][y-shift] not in visited:
            visited.append(matrix[x][y-shift])
        else:
            # 因為遇到不是的之後要往回推一步
            return [x, y-shift+1]
    return [x, y-shift]


def Up(x, y):
    shift = 0
    for shift in range(x):
        # 如果目前這個格子還沒拜訪過，就把它加進拜訪名單裡頭
        if matrix[x-shift][y] not in visited:
            visited.append(matrix[x-shift][y])
        else:
            # 因為遇到不是的之後要往回推一步
            return [x-shift+1, y]
    return [x-shift, y]


# 各種測資
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
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
#     [1, 2, 3, 4]
# ]
# matrix = [
#     [1, 2, 3, 4, 5, 6],
#     [7, 8, 9, 10, 11, 12],
#     [13, 14, 15, 16, 17, 18],
#     [19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30]
# ]
# matrix = [
#     [2, 3, 4],
#     [5, 6, 7],
#     [8, 9, 10],
#     [11, 12, 13],
#     [14, 15, 16]
# ]

m = len(matrix)
n = len(matrix[0])

ref = [x for i in matrix for x in i]
visited = []
x_position, y_position = 0, 0

# 如果所有點都還沒有拜訪完，就繼續拜訪，我用集合下去做
while set(visited) != set(ref):
    # 回傳的位置要移動，為下一個準備，往右走到底之後，下一步是往下走，x座標+1
    x_position, y_position = Right(x_position, y_position)
    x_position += 1

    # 這個檢查是要解決只有一個列向量的情況，像是[1, 2, 3, 4]，這種，往右走到底就
    # 不用再走了，所以當座標超出矩陣範圍的話，就直接跳出去，阿這種情況就只會發生
    # 在最一開始望右走的情況會遇到，也就是只有一個列向量。
    if x_position >= m or y_position >= n:
        break

    # 往下走完之後y座標往左移一格
    x_position, y_position = Down(x_position, y_position)
    y_position -= 1

    # 往左走完之後x座標往上一格
    x_position, y_position = Left(x_position, y_position)
    x_position -= 1

    # 往上走完之後y座標往右一格
    x_position, y_position = Up(x_position, y_position)
    y_position += 1

print visited
