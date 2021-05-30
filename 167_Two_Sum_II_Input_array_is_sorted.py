#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# 2Sum

# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
numbers = [2, 7, 11, 15]
target = 9

# Output: [1,3]
numbers = [2, 3, 4]
target = 6

# Output: [1,2]
numbers = [-1, 0]
target = -1

left = 0
right = len(numbers) - 1
while left < right:
    Sum = numbers[left] + numbers[right]
    # Since array is already sorted, if sum is too much, then we move right
    # backwards
    if Sum > target:
        right -= 1
    # if Sum is less than target, we move left pointer forward
    elif Sum < target:
        left += 1
    else:
        break
print [left+1, right+1]
