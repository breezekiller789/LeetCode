#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sort-characters-by-frequency/

# 1. Hashing

# =======Code========

s = "tree"
s = "Aabb"
hashTable = {}

for char in s:
    if char not in hashTable:
        hashTable[char] = 1
    else:
        hashTable[char] += 1
chars = sorted(hashTable.items(), reverse=1, key=lambda x: x[1])
String = ""
for element in chars:
    char, count = element
    String += char*count
print String
