#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/single-element-in-a-sorted-array/

# Use XOR operation, A xor A = 0, use this concept. Since there is always pairs
# in the list, so if we XOR until the end, there will be left over the only one
# single element, which exactly what we want


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
nums = [3, 3, 7, 7, 10, 11, 11]

x = nums[0]
for num in nums[1:]:
    x ^= num
print x
