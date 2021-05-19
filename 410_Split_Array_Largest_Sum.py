#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/split-array-largest-sum/

# DP[i][j] means nums[0]~nums[j] split into i-1

nums = [7, 2, 5, 10, 8]
m = 2
# nums = [1, 2, 3, 4, 5]
# m = 2
# nums = [1, 4, 4]
# m = 3

length = len(nums)
dp = [[float("inf") for _ in range(length)] for _ in range(m+1)]
Sums = [0] * length
Sum = 0
for i, num in enumerate(nums):
    Sum += num
    Sums[i] = Sum

for i in range(length):
    dp[1][i] = Sums[i]

for i in range(2, m+1):
    for j in range(i-1, length):
        for k in range(j):
            dp[i][j] = min(dp[i][j], max(dp[i-1][k], Sums[j]-Sums[k]))
print dp[m][length-1]
