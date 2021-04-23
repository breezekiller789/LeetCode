#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/burst-balloons/

# 1. select the smallest from the list but not including the first/last element,
# so we have to do some boundry checking here.
# 2. if list[1:-1] is not null, then we select smallest, if null, then we choose
# smalles from first/last

# =========Code===========


def Pick_Smallest(Nums):
    Min = (float("inf"), 0)
    for idx, i in enumerate(Nums):
        if i < Min[0]:
            Min = i, idx+1
    return Min


nums = [3, 1, 5, 8]
nums = [1, 5]
nums = [9, 76, 64, 21, 97, 60]
Sum = 0
while nums[1:-1]:
    smallestNum, idx = Pick_Smallest(nums[1:-1])
    Sum += nums[idx-1]*nums[idx]*nums[idx+1]
    del nums[idx]
    # print nums, smallestNum
if nums[0] > nums[-1]:
    Sum += nums[0]*nums[-1]+nums[0]
else:
    Sum += nums[-1]*nums[0]+nums[-1]
print Sum
