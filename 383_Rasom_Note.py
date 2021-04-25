#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/ransom-note/

# 1. hash all characters, using dictionary, each key is character, value is
# counts
# 2. see ransomNote's hash table, see if the counts and characters are matching

# =========Code==========

ransomNote = "a"
magazine = "b"
# ransomNote = "aa"
# magazine = "ab"
ransomNote = "aa"
magazine = "aab"

noteHashTable = dict()
magazinHashTable = dict()
for char in ransomNote:
    if char in noteHashTable:
        noteHashTable[char] += 1
    else:
        noteHashTable[char] = 1

for char in magazine:
    if char in magazinHashTable:
        magazinHashTable[char] += 1
    else:
        magazinHashTable[char] = 1

# print noteHashTable, magazinHashTable

for element in noteHashTable:
    if element not in magazinHashTable \
            or noteHashTable[element] > magazinHashTable[element]:
        print False
        exit()
print True
