#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Hashing

# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2)
nums = [8, 1, 2, 2, 3]
# [1, 2, 2, 3, 8]

# Output: [2,1,0,3]
nums = [6, 5, 4, 8]

# Output: [0,0,0,0]
# nums = [7, 7, 7, 7]

# Output: [1,0,3,1,4]
# nums = [6, 3, 7, 6, 9]

hashTable = collections.defaultdict(list)
result = [-1 for _ in range(len(nums))]

for i, num in enumerate(nums):
    if num not in hashTable:
        hashTable[num] = [i, 1]
    else:
        hashTable[num][1] += 1
Sorted = sorted(nums)
for i, num in enumerate(Sorted):
    if i > 0 and num == Sorted[i-1]:
        continue
    result[hashTable[num][0]] = i

for i in range(1, len(nums)):
    if result[i] == -1:
        result[i] = result[hashTable[nums[i]][0]]
print result
