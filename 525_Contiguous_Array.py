#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/contiguous-array/

# This question has only binary value, so it gotta be something to it, and it
# is, so, to balance 0/1, if we change 0 to -1, then we get the sum of 0. That's
# basicly the idea, so, if we get a variable called count, then sum til the end,
# if we get an 0, that means we get a valid contiguous subarray. But we have to
# get the length so we have to use a hash table to store the current index.


nums = [0, 1]
nums = [0, 1, 0]
nums = [1, 0, 0, 1, 0]
# nums = [0, 0, 1, 0, 0, 0, 1, 1]
# nums = [0, 0, 0, 1, 1, 1, 0]


Count = 0
HashTable = {0: 0}
maxLength = 0
for idx, num in enumerate(nums, 1):
    # Encounter 0, minus 1
    if not num:
        Count -= 1
    # Encounter 1, add 1
    else:
        Count += 1
    if Count in HashTable:
        maxLength = max(maxLength, idx-HashTable[Count])
    else:
        HashTable[Count] = idx
print maxLength
