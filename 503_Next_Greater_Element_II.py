#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/next-greater-element-ii/

# 1. Got TLE

nums = [1, 2, 1]
# nums = [1, 2, 3, 4, 3]
nums = [5, 4, 3, 2, 1]

Ans = [0 for i in nums]

for i, numi in enumerate(nums):
    if numi == max(nums):
        Ans[i] = -1
        continue
    foundGreater = False
    j = i + 1
    while j < len(nums):
        # print i, j
        if nums[j] > nums[i]:
            foundGreater = True
            Ans[i] = nums[j]
            break
        j += 1
    if not foundGreater:
        for num in nums[:i]:
            if num > numi:
                Ans[i] = num
                break
print Ans
