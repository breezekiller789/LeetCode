#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Binary search

# Output: [3,4]
nums = [5, 7, 7, 8, 8, 10]
target = 8

# Output: [-1,-1]
nums = [5, 7, 7, 8, 8, 10]
target = 6

# Output: [-1,-1]
nums = [5, 7, 7, 8, 8, 10]
target = 0


def FindInterval(nums, startIndex, target):
    left = startIndex - 1
    right = startIndex + 1
    length = len(nums)
    while left >= 0 and right < length and nums[left] == target and \
            nums[right] == target:
        left -= 1
        right += 1
    while left >= 0 and nums[left] == target:
        left -= 1
    while right < length and nums[right] == target:
        right += 1
    return [left+1, right-1]


low = 0
high = len(nums) - 1

while low <= high:
    mid = (low+high)/2
    if nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        print FindInterval(nums, mid, target)
        exit()
print [-1, -1]
