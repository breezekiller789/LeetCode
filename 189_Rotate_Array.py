#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/rotate-array/

# pop屁股，然後新增在頭，就這樣而已。

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
nums = [-1, -100, 3, 99]
k = 2

# =========Code Starts===========

for i in range(k):
    nums.insert(0, nums.pop())
print nums
