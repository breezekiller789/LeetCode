#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

# 方法就是走一次陣列，然後紀錄最大跟第二大的，還有最大值的index
# 然後最後只要檢查最大值有沒有大於第二大的兩倍。

# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
nums = [3, 6, 1, 0]

# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
# nums = [1, 2, 3, 4]

# Output: 0
# Explanation: 1 is trivially at least twice the value as any other number
# because there are no other numbers.
# nums = [1]

highest = -1
secondHighest = -1
highestIndex = -1
for i, num in enumerate(nums):
    if num > highest:
        secondHighest = highest
        highest = num
        highestIndex = i
    elif num > secondHighest:
        secondHighest = num

print highestIndex if 2*secondHighest <= highest else -1
