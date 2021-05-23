#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

# https://leetcode.com/problems/expressive-words/

# Output: 1
s = "heeellooo"
words = ["hello", "hi", "helo"]

hashTable = collections.defaultdict()
for i, char in enumerate(s):
    if char not in hashTable:
        hashTable[char] = [i]
    else:
        hashTable[char].append(i)

currentWordHash = dict()

Count = 0
for word in words:
    for char in word:
        if char not in hashTable:
            break

    else:
        Count += 1
