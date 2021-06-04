#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/arithmetic-slices/

# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and
# [1,2,3,4] itself
nums = [1, 2, 3, 4]

# Output: 0
nums = [1]


def RecursiveArithmetic(nums, start):
    if start < 2:
        return 0
    elif start == len(nums):
        return 1
    elif start > len(nums):
        return 0
    Sum = 0
    if nums[start] - nums[start-1] == nums[start-1] - nums[start-2]:
        Sum += RecursiveArithmetic(nums, start+1)+1
    return Sum


print RecursiveArithmetic(nums, 2)
