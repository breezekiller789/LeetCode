#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/3sum-closest/

# 跟3Sum很像

# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
nums = [-1, 2, 1, -4]
# [-4, -1, 1, 2]
target = 1
length = len(nums)
nums.sort()

Min = [float("inf"), None]  # 左邊放實際最短距離，右邊放本人
for i, pivot in enumerate(nums[:-2]):
    left = i + 1
    right = length - 1
    while left < right:
        Sum = pivot + nums[left] + nums[right]
        distance = abs(Sum-target)
        if distance < Min[0]:
            Min = [distance, Sum]
        if Sum > target:
            right -= 1
        elif Sum < target:
            left += 1
        else:
            print Sum
            exit()
print Min[1]
