#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/burst-balloons/

# 1. select the smallest from the list but not including the first/last element,
# so we have to do some boundry checking here.
# 2. if list[1:-1] is not null, then we select smallest, if null, then we choose
# smalles from first/last

# =========Code===========


# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
nums = [3, 1, 5, 8]

# Output: 10
# nums = [1, 5]

# nums = [9, 76, 64, 21, 97, 60]

nums = [8, 2, 6, 8, 9, 8, 1, 4, 1, 5, 3, 0, 7, 7, 0, 4, 2, 2, 5, 5]


# 我覺得我快解出來了，但是遇到上面這個測資會TLE
def RecursiveBurst(nums, alreadyChecked):
    length = len(nums)
    if length == 1:
        return nums[0]
    if tuple(nums) in alreadyChecked:
        return alreadyChecked[tuple(nums)]
    maxPoint = float("-inf")
    # 從第一個氣球開始搓，然後看搓哪一個氣球分數最高
    for i in range(length):
        if tuple(nums[:i]+nums[i+1:]) in alreadyChecked:
            ret = alreadyChecked[tuple(nums[:i]+nums[i+1:])]
        else:
            ret = RecursiveBurst(nums[:i]+nums[i+1:], alreadyChecked)
        left = 1
        mid = nums[i]
        right = 1
        if i >= 1:
            left = nums[i-1]
        if i+1 < length:
            right = nums[i+1]
        currentPoints = left * mid * right
        maxPoint = max(maxPoint, ret+currentPoints)
        alreadyChecked[tuple(nums[:i]+nums[i+1:])] = ret
    alreadyChecked[tuple(nums)] = maxPoint
    return maxPoint


alreadyChecked = dict()
print RecursiveBurst(nums, alreadyChecked)
# print alreadyChecked
