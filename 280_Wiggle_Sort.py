#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/wiggle-sort/

# 1. the regularity is, for all even index, is less then right side, if false,
# swap them
# 2. if current index is odd, then it should greater than the next value, if
# false, swap them

# =========Code============

nums = [3, 5, 2, 1, 6, 4]


def swap(i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


for idx, num in enumerate(nums[:-1]):
    if idx % 2 == 0:
        if nums[idx] > nums[idx+1]:
            swap(idx, idx+1)
    else:
        if nums[idx] < nums[idx+1]:
            swap(idx, idx+1)
print nums
