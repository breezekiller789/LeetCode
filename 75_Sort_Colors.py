#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/sort-colors/

# 題目規定in place，可以用的就insertion sort, bubble sort, selection sort...
# 我用Insertion sort

nums = [2, 0, 2, 1, 1, 0]

length = len(nums)

# Insertion Sort
for i in range(1, length):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key

print nums
