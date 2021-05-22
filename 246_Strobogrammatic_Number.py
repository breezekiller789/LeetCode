#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/strobogrammatic-number/

# Output: True
# num = "69"

# Output: True
num = "88"

# Output: False
num = "962"

# Output: true
num = "1698"

looksTheSameWhenUpsideDown = {"6": "9", "8": "8", "9": "6", "1": "1", "0": "0"}
length = len(num)
for i, char in enumerate(num):
    if char not in looksTheSameWhenUpsideDown or num[length-i-1] not in looksTheSameWhenUpsideDown:
        print False
        exit()
    elif char != looksTheSameWhenUpsideDown[num[length-i-1]]:
        print False
        exit()
print True
