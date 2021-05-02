#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

'''
Use the same concept of Question 442, in place, linear
'''

# ========Code=========

nums = [4, 3, 2, 7, 8, 2, 3, 1]
length = len(nums)

for idx in range(length):
    index = abs(nums[idx])-1
    nums[index] = -abs(nums[index])
Ans = []
for idx, num in enumerate(nums):
    if num > 0:
        Ans.append(idx+1)
print Ans
