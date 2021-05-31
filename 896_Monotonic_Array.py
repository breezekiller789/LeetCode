#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/monotonic-array/

# 設定flag

# Output: true
nums = [1, 2, 2, 3]

# Output: true
# nums = [6, 5, 4, 4]

# Output: false
# nums = [1, 3, 2]

# Output: true
# nums = [1, 2, 4, 5]

# Output: true
# nums = [1, 1, 1]

# Output: false
# nums = [2, 2, 2, 1, 4, 5]

increasing = False
decreasing = False

length = len(nums)

if length <= 2:
    print True
    exit()

for i, num in enumerate(nums[1:], start=1):
    if num > nums[i-1] and increasing:
        increasing = True
        continue
    elif num < nums[i-1] and decreasing:
        decreasing = True
        continue
    elif num > nums[i-1] and decreasing or num < nums[i-1] and increasing:
        print False
        exit()
    if num > nums[i-1]:
        increasing = True
    elif num < nums[i-1]:
        decreasing = True
print True
