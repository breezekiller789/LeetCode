#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# https://leetcode.com/problems/perfect-squares/


def PerfectSquareRecursive(n, squareNumbers):
    if n == 0:
        return 0
    if DP[n]:
        return DP[n]+1
    Min = float("inf")
    for i in range(len(squareNumbers)-1, -1, -1):
        newTarget = n - squareNumbers[i]
        if newTarget >= 0:
            Min = min(Min,
                      PerfectSquareRecursive(newTarget, squareNumbers))
        DP[n] = Min + 1
    return DP[n]


n = 12
# n = 13
# n = 18
# n = 5
# n = 6
# n = 1000
# n = 11
# n = 5

# 這是用iterative的DP
DP = [float("inf")] * (n + 1)
DP[0] = 0
squareNumbers = [i**2 for i in range(1, int(math.sqrt(n))+1)]
for i in range(1, n+1):
    for squarenumber in squareNumbers:
        if i < squarenumber:
            break
        DP[i] = min(DP[i], DP[i-squarenumber]+1)
print DP[n]

# 打開這個來用遞迴的DP，但是這個還有bug，像是48，應該是3，我會印4
# DP = [None] * (n + 1)
# DP[0] = 0
# squareNumbers = [i**2 for i in range(1, int(math.sqrt(n))+1)]
# print PerfectSquareRecursive(n, squareNumbers)
