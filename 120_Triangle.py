#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/triangle/

# 用DP，其實就是從頭加到尾，從最上面加到最下面，然後紀錄最小的，就這樣而已。


# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11
# (underlined above).
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

# Output: -10
triangle = [[-10]]

for i, row in enumerate(triangle[1:], start=1):
    length = len(row)
    for j in range(length):
        # 如果是在邊界，直接加上去
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
            continue
        # 如果是在邊界，直接加上去
        elif j == len(row)-1:
            triangle[i][j] += triangle[i-1][j-1]
        # 會來這裡就是不在邊界上，就做類似relax
        else:
            triangle[i][j] = min(triangle[i-1][j-1],
                                 triangle[i-1][j]) + triangle[i][j]
print min(triangle[-1])
