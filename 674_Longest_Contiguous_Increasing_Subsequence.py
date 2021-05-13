#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Simple array manipulation


nums = [1, 3, 5, 4, 7]
nums = [2, 2, 2, 2, 2]
Count = 1
Max = 0
for idx, num in enumerate(nums[1:], 1):
    if num - nums[idx-1] > 0:
        Count += 1
    else:
        Count = 1
    Max = max(Max, Count)
print Max
