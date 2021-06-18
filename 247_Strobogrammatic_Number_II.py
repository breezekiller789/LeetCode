#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/strobogrammatic-number-ii/

# Output: ["11","69","88","96"]
n = 2

# Output: ["0","1","8"]
# n = 1

n = 4


def RecursiveGenerate(n, pairTable):
    if n == 2:
        return ["00", "11", "69", "88", "96"]
    childStrings = RecursiveGenerate(n-2, pairTable)
    currentLevelStrings = []
    for num in pairTable:
        for i, string in enumerate(childStrings):
            currentLevelStrings.append(str(num) + string + str(pairTable[num]))
    return currentLevelStrings


pairTable = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

if n % 2 == 0:
    print RecursiveGenerate(n, pairTable)
else:
    # insert 1, 8 into the strings in the middle
    # ["11", "69", "88", "96"]
    # -> ["111", "619", "818", "916", "181", "689", "888", "986"]
    childStrings = RecursiveGenerate(n-1, pairTable)
    resultStrings = []
    length = (n-1) / 2
    for string in childStrings:
        resultStrings.append(string[:length] + "0" + string[length:])
        resultStrings.append(string[:length] + "1" + string[length:])
        resultStrings.append(string[:length] + "8" + string[length:])
    print resultStrings
