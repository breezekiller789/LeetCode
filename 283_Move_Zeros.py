#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/move-zeroes/
nums = [0, 1, 0, 3, 12]
Zero_Count = nums.count(0)
for i in range(Zero_Count):
    nums.remove(0)
nums.extend([0 for i in range(Zero_Count)])
print nums
