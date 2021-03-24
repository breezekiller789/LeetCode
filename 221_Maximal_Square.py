#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximal-square/

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]


# =========Code Starts========


def Check_Kernel(size, start_x, start_y):
    for shift_x in range(size):
        for shift_y in range(size):
            if matrix[start_x+shift_x][start_y+shift_y] == "0":
                return False
    return True


m = len(matrix)
n = len(matrix[0])
kernel_size = min(m, n)
for size in xrange(kernel_size, 0, -1):
    for start_x in range(m-size+1):
        for start_y in range(n-size+1):
            if Check_Kernel(size, start_x, start_y):
                print size * size
                exit()
