#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/total-hamming-distance/

# 1. Find all combinations
# 2. Each combination, calculate the hamming distance
# 3. Hamming distance: XOR + Count 1 in binary representation

# ==========Code===========


def HammingDistance(x, y):
    x ^= y
    count = 0
    while x:
        x = x & (x-1)
        count += 1
    return count


nums = [4, 14, 2]   # 6
nums = [4, 14, 4]   # 4

Sum = 0
for i, numi in enumerate(nums[:-1]):
    for j, numj in enumerate(nums[i+1:]):
        Sum += HammingDistance(numi, numj)
print Sum
