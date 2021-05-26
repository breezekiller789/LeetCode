#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/flipping-an-image/

# 每一列每一列作，先反過來，然後再把每一個value跟1做XOR

# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
image = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 0, 0]
]

# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row:
# [
# [0,0,1,1],
# [1,0,0,1],
# [1,1,1,0],
# [0,1,0,1]
# ].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
image = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 0]
]
for i, row in enumerate(image):
    for j, num in enumerate(row[::-1]):
        image[i][j] = num ^ 1
print image
