#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/4sum/

# 其實跟3Sum很像，就是說每一次我都固定一個值，然後再套用3Sum的方法，選pivot,
# left, right這樣去算總和，然後當然還是要先排序。

# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
nums = [1, 0, -1, 0, -2, 2]
target = 0
# [-2, -1, 0, 0, 1, 2]

# Output: [[2, 2, 2, 2]]
nums = [2, 2, 2, 2, 2]
target = 8

nums.sort()
length = len(nums)
result = []
Seen = set()
for i, num in enumerate(nums[:-3]):
    for j, pivot in enumerate(nums[i+1:-2], start=i+1):
        left = j + 1
        right = length - 1
        while left < right:
            Sum = num + pivot + nums[left] + nums[right]
            if Sum > target:
                right -= 1
            elif Sum < target:
                left += 1
            else:
                tmp = [num, pivot, nums[left], nums[right]]
                if tuple(tmp) not in Seen:
                    result.append(tmp)
                    Seen.add(tuple(tmp))
                left += 1
                right -= 1
print result
