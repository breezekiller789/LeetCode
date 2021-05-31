#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/squares-of-a-sorted-array/

# 用two pointer，會比較快，也或者可以直接把全部都給他平方然後再排序也可以。

# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100]
nums = [-4, -1, 0, 3, 10]

# Output: [4,9,9,49,121]
# nums = [-7, -3, 2, 3, 11]

left = 0
right = len(nums) - 1
i = 0
result = [0 for _ in range(len(nums))]
while left <= right:
    if abs(nums[left]) > abs(nums[right]):
        num = nums[left]
        left += 1
    else:
        num = nums[right]
        right -= 1
    result[i] = num ** 2
    i += 1
print result[::-1]
