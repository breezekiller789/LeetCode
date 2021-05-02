#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# ========Code=========

nums = [4, 3, 2, 7, 8, 2, 3, 1]

# Method 1, use hashing
# hashTable = {}
# for num in nums:
#     if str(num) not in hashTable:
#         hashTable[str(num)] = 1
#     else:
#         hashTable[str(num)] += 1
# Ans = []
# for element in hashTable:
#     if hashTable[element] == 2:
#         Ans.append(int(element))
# print Ans

# Method 2, mark visited elements in the input array itself. The idea is, since
# each value in the array is bounded by n, so if we substract each value by 1,
# then we can get the index of array, for example, if we are now getting 4,
# 4-1=3, then 3 is the index of array, we visit that element, make that element
# negative, and that indicates we've visited the element, so, if we get a
# duplicate 4, then we visit index 3 again, if we have a negative element, that
# means we have already visited this element, so we add current value to the
# answer array.

# Side note: Keep in mind, this question has a important requirement, and that
# is the 1 <= nums[i] <= n, if this doesn't hold, then we cannot use this method

Ans = []
for num in nums:
    index = abs(num)-1  # Get the index of input array
    if nums[index] < 0:
        Ans.append(abs(num))
    else:
        nums[index] = -nums[index]
print Ans
