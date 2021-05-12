#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/robot-return-to-origin/

# Solve by using hash tables

moves = "UD"
# moves = "LL"
# moves = "RRDD"
# moves = "LDRRLRUULR"

hashTable = dict()
hashTable["U"] = 0
hashTable["D"] = 0
hashTable["L"] = 0
hashTable["R"] = 0

for char in moves:
    hashTable[char] += 1

if hashTable["L"] - hashTable["R"] != 0 or hashTable["D"] - hashTable["U"] != 0:
    print False
    exit()
print True
