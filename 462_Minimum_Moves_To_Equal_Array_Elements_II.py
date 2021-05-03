#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

# 1. Sort the list first, and get the middle element, call it avg
# 2. Scan through the list, and Sum up the differences.

# =======Code=======

nums = [1, 2, 3]        # 2
# nums = [1, 10, 2, 9]    # 16
# nums = [1, 0, 0, 8, 6]  # 14

nums.sort()     # Sort first
Avg = nums[len(nums)//2]    # Get the middle element

Sum = 0
for num in nums:
    Sum += abs(num-Avg)
print Sum
