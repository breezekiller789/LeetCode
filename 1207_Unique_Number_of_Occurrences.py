#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/unique-number-of-occurrences/

# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
# have the same number of occurrences.
arr = [1, 2, 2, 1, 1, 3]

# Output: false
# arr = [1, 2]

# Output: true
# arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

hashTable = dict()
for num in arr:
    if num not in hashTable:
        hashTable[num] = 1
    else:
        hashTable[num] += 1

numberSeen = set()

for num in hashTable:
    if hashTable[num] not in numberSeen:
        numberSeen.add(hashTable[num])
    else:
        print False
        exit()
print True
