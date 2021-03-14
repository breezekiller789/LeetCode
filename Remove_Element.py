#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/remove-element/

nums = [3, 2, 2, 3]
val = 3
for i in range(nums.count(val)):
    nums.remove(val)
print nums
