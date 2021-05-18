#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-anagram-mappings/

nums1 = [12, 28, 46, 32, 50]
nums2 = [50, 12, 32, 46, 28]
# Output
# [1, 4, 3, 2, 0]

hashTable = dict()
for index, num in enumerate(nums2):
    if num not in hashTable:
        hashTable[num] = index
Indeces = []
for num in nums1:
    Indeces.append(hashTable[num])
print Indeces
