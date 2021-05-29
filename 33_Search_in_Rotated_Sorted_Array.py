#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Output: 4
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# Output: -1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

# Output: -1
# nums = [1]
# target = 0

length = len(nums)
low = 0
high = length - 1
while low <= high:
    mid = (low+high) / 2
    # 找到
    if nums[mid] == target:
        print mid
        exit()
    # 如果左半邊的順序是排序好的，我們就進去看看
    elif nums[low] <= nums[mid]:
        # 如果目標是在左半邊，就縮減high
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        # 如果目標不在左半邊，就縮減low
        else:
            low = mid + 1
    # 如果右半邊的順序是排序好的，我們就進去看看
    elif nums[mid] <= nums[high]:
        # 如果目標是在右手邊就縮減low
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        # 如果目標不在右手邊，就縮減high
        else:
            high = mid - 1
print -1
