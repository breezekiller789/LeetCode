#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict

# https://leetcode.com/problems/isomorphic-strings/

# Output: true
s = "egg"
t = "add"

# Output: false
# s = "foo"
# t = "bar"

# Output: true
# s = "paper"
# t = "title"

hashTable = defaultdict()
hashTable1 = defaultdict()

for i, char in enumerate(s):
    if char not in hashTable:
        hashTable[char] = [i]
    else:
        hashTable[char].append(i)
for i, char in enumerate(t):
    if char not in hashTable1:
        hashTable1[char] = [i]
    else:
        hashTable1[char].append(i)
Set1 = set()
Set2 = set()
for char in hashTable:
    Set1.add(tuple(hashTable[char]))
for char in hashTable1:
    Set2.add(tuple(hashTable1[char]))
print Set1 == Set2
