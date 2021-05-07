#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/lonely-pixel-i/


def isLonelyPixel(picture, idx, jdx):
    i = 0
    while i < len(picture):
        if picture[i][jdx] == "B" and i != idx:
            return False
        i += 1
    return True


picture = [
    ["W", "W", "B"],
    ["W", "B", "W"],
    ["B", "W", "W"]
]
# picture = [
#     ["B", "B", "B"],
#     ["B", "B", "B"],
#     ["B", "B", "B"]
# ]
# picture = [
#     ["W", "B", "W", "W"],
#     ["W", "B", "B", "W"],
#     ["W", "W", "W", "W"]
# ]

Count = 0
for idx, row in enumerate(picture):
    if picture[idx].count("B") != 1:
        continue
    for jdx, col in enumerate(row):
        if picture[idx][jdx] == "B":
            if isLonelyPixel(picture, idx, jdx):
                Count += 1
print Count
