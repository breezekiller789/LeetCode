#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-harmonious-subsequence/

nums = [1, 3, 2, 2, 5, 2, 3, 7]
# nums = [1, 2, 3, 4]
# nums = [1, 1, 1, 1]

hashTable = dict()
for num in nums:
    if num not in hashTable:
        hashTable[num] = 1
    else:
        hashTable[num] += 1
myList = hashTable.items()
myList.sort(key=lambda x: x[0])
Sum = 0
Max = 0
for idx, num in enumerate(myList[:-1]):
    if abs(num[0]-myList[idx+1][0]) == 1:
        Sum = max(Sum, num[1]+myList[idx+1][1])
print Sum
