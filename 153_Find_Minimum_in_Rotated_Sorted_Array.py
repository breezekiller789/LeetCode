#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# 變形binary search

# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
nums = [3, 4, 5, 1, 2]

# Output: 0
# Explanation:The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
nums = [4, 5, 6, 7, 0, 1, 2]

# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
nums = [11, 13, 15, 17]

nums = [5, 1, 2, 3, 4]

nums = [7, 1, 2, 3, 4, 5, 6]

low = 0
high = len(nums) - 1
Min = float("inf")
while low < high:
    mid = (low+high) / 2

    # 每一步都要趁機紀錄最小值。
    Min = min(Min, nums[low], nums[mid], nums[high])

    # 如果左指標大於右邊，代表最小值只會在右半邊。
    if nums[low] > nums[high]:
        low = mid + 1
    # 到這裡，我左指標到右指標就會是遞增的，這時候最小值還是有可能在左指標的左邊
    elif Min < nums[low] or nums[low-1] < nums[low]:
        low /= 2
        high = mid - 1
    # 以上情況都不符合，就代表找到最小值了
    else:
        break
print Min
