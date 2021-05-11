#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-product-of-three-numbers/

nums = [1, 2, 3]
nums = [1, 2, 3, 4]
# nums = [-1, -2, -3]

length = len(nums)
Ans = 1
if length == 3:
    for num in nums:
        Ans *= num
    print Ans
    exit()

nums.sort()
print max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
