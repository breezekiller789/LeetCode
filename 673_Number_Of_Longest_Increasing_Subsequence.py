#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

# 我很接近了，現在我可以回傳nums中最長的遞增subsequence，而且不用是連續的！
# 我覺得這樣就是一個DP考題了，因為我就是用DP下去解，但是跟題目要的東西不一樣。

nums = [1, 3, 5, 4, 7]
# nums = [2, 2, 2, 2, 2]

length = len(nums)
dp = [[0 for _ in range(length)] for _ in range(length)]

for idx in xrange(length-1, -1, -1):
    dp[idx][idx] = 1
    for jdx in range(idx+1, length):
        if nums[idx] < nums[idx+1] and nums[jdx] > nums[jdx-1]:
            dp[idx][jdx] = dp[idx+1][jdx-1] + 2
        else:
            dp[idx][jdx] = max(dp[idx+1][jdx], dp[idx][jdx-1])
longestLength = dp[0][length-1]
