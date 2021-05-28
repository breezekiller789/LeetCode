#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/game-of-life/

# 這題就是比較需要注意邊界檢查要仔細。

# Output: [
# [0, 0, 0],
# [1, 0, 1],
# [0, 1, 1],
# [0, 1, 0]
# ]
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

# Output: [
# [1, 1],
# [1, 1]
# ]
# board = [
#     [1, 1],
#     [1, 0]
# ]


def NeighborsThatsAlive(board, startNode, m, n):
    x, y = startNode
    liveCount = 0
    # Up
    if x >= 1 and board[x-1][y] == 1:
        liveCount += 1
    # Right
    if y < n-1 and board[x][y+1] == 1:
        liveCount += 1
    # Down
    if x < m-1 and board[x+1][y] == 1:
        liveCount += 1
    # Left
    if y >= 1 and board[x][y-1] == 1:
        liveCount += 1
    # Up left
    if x >= 1 and y >= 1 and board[x-1][y-1] == 1:
        liveCount += 1
    # Up right
    if x >= 1 and y < n-1 and board[x-1][y+1] == 1:
        liveCount += 1
    # Down right
    if x < m-1 and y < n-1 and board[x+1][y+1] == 1:
        liveCount += 1
    # Down left
    if x < m-1 and y >= 1 and board[x+1][y-1] == 1:
        liveCount += 1
    return liveCount


def Dead(board, startNode, live, m, n):
    if live == 1:
        neighborsAlive = NeighborsThatsAlive(board, startNode, m, n)
        # print startNode, live, neighborsAlive
        # Any live cell with fewer than two live neighbors dies as if caused by
        # under-population
        if neighborsAlive < 2:
            return True

        # Any live cell with two or three live neighbors lives on to the next
        # generation
        if neighborsAlive == 2 or neighborsAlive == 3:
            return False

        # Any live cell with more than three live neighbors dies, as if by
        # over-population
        if neighborsAlive > 3:
            return True
    else:
        neighborsAlive = NeighborsThatsAlive(board, startNode, m, n)
        # print startNode, live, neighborsAlive
        # Any dead cell with exactly three live neighbors becomes a live cell,
        # as if by reproduction.
        if neighborsAlive == 3:
            return False
        else:
            return True


m = len(board)
n = len(board[0])
result = [[0 for _ in range(n)] for _ in range(m)]

for i, row in enumerate(board):
    for j, live in enumerate(row):
        if Dead(board, (i, j), live, m, n):
            result[i][j] = 0
        else:
            result[i][j] = 1
print result
