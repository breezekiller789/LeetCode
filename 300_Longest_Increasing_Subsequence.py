#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-increasing-subsequence/

# Solution: https://www.youtube.com/watch?v=fV-TF4OvZpk
# Time O(n^2)
# Space O(n)
# 這一題我還真不知道怎麼解釋，我也是看影片才會的，因為真的太難想

nums = [10, 9, 2, 5, 3, 7, 101, 18]    # 4
nums = [0, 1, 0, 3, 2, 3]            # 4
# nums = [4, 10, 4, 3, 8, 9]          # 3
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]     # 6

length = len(nums)
dp = [1 for _ in range(length)]
for j in range(1, length):
    for i in range(j):
        if nums[j] > nums[i]:
            dp[j] = max(dp[j], dp[i]+1)
        else:
            continue
print max(dp)
