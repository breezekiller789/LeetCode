#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://leetcode.com/problems/split-array-into-consecutive-subsequences/


nums = [1, 2, 3, 3, 4, 5]           # True
nums = [1, 2, 3, 3, 4, 4, 5, 5]     # True
nums = [1, 2, 3, 4, 4, 5]           # False

occurrence = [0 for _ in range(10)]
for num in nums:
    occurrence[num] += 1
print occurrence
