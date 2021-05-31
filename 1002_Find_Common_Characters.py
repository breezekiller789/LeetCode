#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-common-characters/

# Output: ["e","l","l"]
words = ["bella", "label", "roller"]

# Output: ["c","o"]
# words = ["cool", "lock", "cook"]

intersections = dict()

# 先hash第一個字串
for char in words[0]:
    if char not in intersections:
        intersections[char] = 1
    else:
        intersections[char] += 1

for i in range(1, len(words)):
    tmpDict = dict()
    # 先hash現在這個字串
    for char in words[i]:
        if char not in tmpDict:
            tmpDict[char] = 1
        else:
            tmpDict[char] += 1

    # 用一個新的dict去記錄他們intersection跟tmpDict的共同字元，然後數量擷取少的
    newDict = dict()
    for char in intersections:
        if char in tmpDict:
            newDict[char] = min(tmpDict[char], intersections[char])
    intersections = newDict
print [char for char in intersections for _ in range(intersections[char])]
