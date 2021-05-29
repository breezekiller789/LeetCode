#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/next-permutation/

# Output: [1,3,2]
nums = [1, 2, 3]

# Output: [1,2,3]
nums = [3, 2, 1]

# Output: [1,5,1]
# nums = [1, 1, 5]

# Output: [1]
# nums = [1]

length = len(nums)
for i in range(length-1, -1, -1):
    for j in range(i-1, -1, -1):
        if nums[i] > nums[j]:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            print nums
            exit()
print sorted(nums)
