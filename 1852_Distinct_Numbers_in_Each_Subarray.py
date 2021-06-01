#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/distinct-numbers-in-each-subarray/

# Output: [3,2,2,2,3]
# Explanation: The number of distinct elements in each subarray goes as follows:
# - nums[0:2] = [1,2,3] so ans[0] = 3
# - nums[1:3] = [2,3,2] so ans[1] = 2
# - nums[2:4] = [3,2,2] so ans[2] = 2
# - nums[3:5] = [2,2,1] so ans[3] = 2
# - nums[4:6] = [2,1,3] so ans[4] = 3
nums = [1, 2, 3, 2, 2, 1, 3]
k = 3

# Output: [1,2,3,4]
# Explanation: The number of distinct elements in each subarray goes as follows:
# - nums[0:3] = [1,1,1,1] so ans[0] = 1
# - nums[1:4] = [1,1,1,2] so ans[1] = 2
# - nums[2:5] = [1,1,2,3] so ans[2] = 3
# - nums[3:6] = [1,2,3,4] so ans[3] = 4
# nums = [1, 1, 1, 1, 2, 3, 4]
# k = 4

hashTable = dict()
left = 0
right = 0
result = []
# Sliding window
for num in nums:
    # Shrink the sliding window
    if right >= k:
        result.append(len(hashTable))  # append the size of hash table first
        hashTable[nums[left]] -= 1     # remove 1 in hash table
        if hashTable[nums[left]] == 0:  # if that num is 0, then remove it
            hashTable.pop(nums[left])
        left += 1                       # shrink the sliding window
    if num not in hashTable:
        hashTable[num] = 1
    else:
        hashTable[num] += 1
    right += 1
result.append(len(hashTable))
print result
