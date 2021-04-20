#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/3sum-smaller/

# 1. check if there is multiple 0's, more than 3, if yes, make it 3
# 2. check if len(nums) < 3, if less than 3, return
# 3. Sort the nums
# 4. use the 3Sum method, pick pivot, then set low, high, sum the pivot, low,
# high and see if Sum is less than target, if yes, add it to list, and move low
# forward, if no, move the high backwards and continue

# ===========Code==========
# nums = [-2, 0, 1, 3]
# nums = [-1, 1, -1, -1]
nums = [1, -2, 2, 1, 0]
# nums = [3, 1, 0, -2]
# nums = [0, 0, 0, 0]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-1, 0, 1, 0]
# nums = [-1, -2, -2, -2, 3, 3, 3]
target = 1

nums = sorted(nums)
length = len(nums)
Ans = []
for idx, pivot in enumerate(nums[:-2]):
    low = idx+1
    high = length-1
    while low < high:
        Sum = pivot + nums[low] + nums[high]
        # print nums, pivot, nums[low], nums[high], Sum
        if Sum < target:
            for x in nums[low+1:high+1]:
                if [pivot, nums[low], x] not in Ans:
                    Ans.append([pivot, nums[low], x])
            low += 1
        elif Sum > target:
            high -= 1
        else:
            high -= 1
print Ans
