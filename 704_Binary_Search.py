#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-search/


nums = [-1, 0, 3, 5, 9, 12]
target = 9
nums = [-1, 0, 3, 5, 9, 12]
target = 2

low = 0
high = len(nums)-1
while low <= high:
    mid = (low+high)/2
    if nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        print mid
        exit()
print -1
