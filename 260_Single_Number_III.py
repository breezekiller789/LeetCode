#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/single-number-iii/

# 1. go through the list once, and hash all the numbers
# 2. check the hash table, if all the targets appeared once

# =========Code=========

nums = [1, 2, 1, 3, 2, 5, 3]
# nums = [-1, 0]
hashTable = dict()
appearedOnceNum = []

for num in nums:
    if str(num) not in hashTable:
        hashTable[str(num)] = 1
    else:
        hashTable[str(num)] += 1

for item in hashTable:
    if hashTable[item] == 1:
        appearedOnceNum.append(item)
print appearedOnceNum
