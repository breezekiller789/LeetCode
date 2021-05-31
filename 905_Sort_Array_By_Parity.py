#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sort-array-by-parity/

# Two pointers

# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted
nums = [3, 1, 2, 4]  # [4, 1, 2, 3] -> [4, 2, 1, 3]

left = 0
right = len(nums) - 1

while left < right:
    # Left pointer find odd number
    while nums[left] % 2 == 0 and left < right:
        left += 1

    # Right pointer find even number
    while nums[right] % 2 == 1 and left < right:
        right -= 1

    # Swap them
    nums[left], nums[right] = nums[right], nums[left]
print nums
