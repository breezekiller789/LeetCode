#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximal-rectangle/

# 我直接抄解答，實在不可能想得出來。直接看影片講解
# https://www.youtube.com/watch?v=g8bSdXCG-lA


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
if not matrix:
    print 0
    exit()

m = len(matrix)
n = len(matrix[0])

left = [0] * n      # initialize left as the leftmost boundary possible
right = [n] * n     # initialize right as the rightmost boundary possible
height = [0] * n

maxarea = 0

for i in range(m):

    cur_left, cur_right = 0, n
    # update height
    for j in range(n):
        if matrix[i][j] == '1':
            height[j] += 1
        else:
            height[j] = 0
    # update left
    for j in range(n):
        if matrix[i][j] == '1':
            left[j] = max(left[j], cur_left)
        else:
            left[j] = 0
            cur_left = j + 1
    # update right
    for j in range(n-1, -1, -1):
        if matrix[i][j] == '1':
            right[j] = min(right[j], cur_right)
        else:
            right[j] = n
            cur_right = j
    # update the area
    for j in range(n):
        maxarea = max(maxarea, height[j] * (right[j] - left[j]))

print maxarea
