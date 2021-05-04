#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/max-consecutive-ones/

nums = [1, 1, 0, 1, 1, 1]
nums = [1, 0, 1, 1, 0, 1]

Count = 0
Max = 0
for num in nums:
    if num:
        Count += 1
    else:
        Count = 0
    Max = max(Max, Count)       # Get the current maximum
print Max
