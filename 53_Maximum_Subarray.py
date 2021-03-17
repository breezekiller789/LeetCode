#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximum-subarray/
# 影片講解Kadane's Algorithm

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Curren_max = nums[0]
Global_max = nums[0]
for i in range(1, len(nums)):
    Curren_max = max(nums[i], Curren_max+nums[i])
    if Curren_max > Global_max:
        Global_max = Curren_max
print Global_max
