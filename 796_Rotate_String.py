#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/rotate-string/

# Hashing


# Output: true
s = 'abcde'
goal = 'cdeab'

# Output: false
s = 'abcde'
goal = 'abced'

hashTable = dict()
for i in range(1, len(s)):
    prefix = s[:i]
    suffix = s[i:]
    hashTable[prefix] = suffix
for i in range(1, len(goal)):
    prefix = goal[:i]
    suffix = goal[i:]
    if prefix in hashTable and hashTable[prefix] == suffix or\
            suffix in hashTable and hashTable[suffix] == prefix:
        print True
        exit()
print False
