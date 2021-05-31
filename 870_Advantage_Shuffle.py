#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/advantage-shuffle/

# 有bug

# Output: [2,11,7,15]
nums1 = [2, 7, 11, 15]
nums2 = [1, 10, 4, 11]

# Output: [24,32,8,12]
# nums1 = [12, 24, 8, 32]
# nums2 = [13, 25, 32, 11]

# Sort nums1
# loop through nums2 one by one
# apply binary search


def Find(nums, target):
    if nums[0] > target or target > max(nums):
        ret = nums[0]
        del nums[0]
        return ret

    index = 1
    while index < len(nums) and nums[index] < target:
        index *= 2

    if index >= len(nums):
        ret = nums[-1]
        del nums[-1]
        return ret
    if nums[index] == target:
        ret = nums[index]
        del nums[index]
        return ret

    while nums[index] > target:
        index -= 1
    ret = nums[index+1]
    del nums[index+1]
    return ret


nums1.sort()
result = []
for num in nums2:
    res = Find(nums1, num)
    result.append(res)
print result
