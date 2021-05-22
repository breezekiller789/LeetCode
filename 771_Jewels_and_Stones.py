#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/jewels-and-stones/

# Output: 3
jewels = "aA"
stones = "aAAbbbb"

# Output: 0
# jewels = "z"
# stones = "ZZ"

hashJewels = set()
for jewel in jewels:
    hashJewels.add(jewel)

Count = 0
for stone in stones:
    if stone in hashJewels:
        Count += 1
print Count
