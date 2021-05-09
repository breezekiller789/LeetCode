#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subarray-sum-equals-k/

# Very good question


nums = [1, 1, 1]
k = 2
# nums = [1, 2, 3]
# k = 3
# nums = [1, 2, 1, 3]
# k = 3

length = len(nums)
Sum = 0
Count = 0
hashTable = {0: 1}
for num in nums:
    Sum += num
    Count += hashTable.get(Sum-k, 0)
    hashTable[Sum] = hashTable.get(Sum, 0) + 1
print Count
