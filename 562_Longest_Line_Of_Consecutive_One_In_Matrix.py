#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

# 3-D Dp array, pretty amazing, pretty hard to come up with


mat = [
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
]
# mat = [
#     [1, 1, 1, 1],
#     [0, 1, 1, 0],
#     [0, 0, 0, 1]
# ]
# mat = [
#     [0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 1],
#     [0, 0, 0, 1, 0],
#     [1, 0, 1, 1, 1],
#     [1, 0, 0, 0, 1]
# ]
# mat = [
#     [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
#     [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
#     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
#     [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
#     [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
# ]

Rows = len(mat)
Cols = len(mat[0])
DP = [[[0 for _ in range(Cols)] for _ in range(Rows)] for _ in range(4)]
Max = 0
for idx in range(Rows):
    for jdx in range(Cols):
        if mat[idx][jdx] == 1:
            # Horizontal
            if jdx > 0:
                DP[0][idx][jdx] = DP[0][idx][jdx-1] + 1
            else:
                DP[0][idx][jdx] = 1

            # Vertical
            if idx > 0:
                DP[1][idx][jdx] = DP[1][idx-1][jdx] + 1
            else:
                DP[1][idx][jdx] = 1

            # Diagonal
            if idx > 0 and jdx > 0:
                DP[2][idx][jdx] = DP[2][idx-1][jdx-1] + 1
            else:
                DP[2][idx][jdx] = 1

            # Anti-diagonal
            if idx > 0 and jdx < Cols-1:
                DP[3][idx][jdx] = DP[3][idx-1][jdx+1] + 1
            else:
                DP[3][idx][jdx] = 1
        Max = max(Max, DP[0][idx][jdx], DP[1][idx][jdx], DP[2][idx][jdx],
                  DP[3][idx][jdx])
print Max
