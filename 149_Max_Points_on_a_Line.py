#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/max-points-on-a-line/

# 有bug，就是如果有相同的斜率但是並不是在同一條線上，也就是平行線，這樣就會錯。
# 找時間修...

# Output: 3
points = [
    [1, 1],
    [2, 2],
    [3, 3]
]

# Output: 4
points = [
    [1, 1],
    [3, 2],
    [5, 3],
    [4, 1],
    [2, 3],
    [1, 4]
]

# points.sort()
Slopes = dict()
for i, start in enumerate(points):
    x1, y1 = start
    for j, end in enumerate(points[i+1:], start=i+1):
        x2, y2 = end
        if x2-x1 == 0:
            slope = float("inf")
        else:
            slope = float((y2-y1)) / float((x2-x1))
        # print start, end, slope
        if slope not in Slopes:
            Slopes[slope] = set()
            Slopes[slope].add(tuple(start))
            Slopes[slope].add(tuple(end))
        else:
            Slopes[slope].add(tuple(start))
            Slopes[slope].add(tuple(end))
Max = 0
for element in Slopes:
    Max = max(Max, len(Slopes[element]))
print Max
