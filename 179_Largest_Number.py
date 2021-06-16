#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/largest-number/

# Output: "210"
nums = [10, 2]

# Output: "9534330"
# nums = [3, 30, 34, 5, 9]

# Output: "1"
nums = [1]

# Output: "10"
nums = [10]


def evaluate(n1, n2):
    return str(n1)+str(n2) > str(n2)+str(n1)


for i in range(0, len(nums)-1):
    for j in range(i, len(nums)-1-i):
        # evaluate() returns True if str(nums[j])+str(nums[j+1]) >
        # str(nums[j+1])+str(nums[j])
        if evaluate(nums[j], nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]

# Cover [0, 0, 0]這種
while nums.count(0) == len(nums) and nums.count(0) > 1:
    nums.remove(0)
print "".join(map(str, nums[::-1]))
