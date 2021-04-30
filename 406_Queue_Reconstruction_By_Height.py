#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/queue-reconstruction-by-height/submissions/

# 1. sort the array with height, from high to low and k value from low to high
# 2. insert element to empty array according to k value

# =============Code===============

people = [
    [7, 0],
    [4, 4],
    [7, 1],
    [5, 0],
    [6, 1],
    [5, 2]
]
people = [
    [6, 0],
    [5, 0],
    [4, 0],
    [3, 2],
    [2, 2],
    [1, 4]
]
people.sort(key=lambda x: (-x[0], x[1]))
output = []
for p in people:
    output.insert(p[1], p)
print output
