#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/merge-intervals/


intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]

Ans = []
for interval in sorted(intervals):
    if not Ans or interval[0] > Ans[-1][-1]:
        Ans.append(interval)
    else:
        # Merge
        Ans[-1] = [Ans[-1][0], max(Ans[-1][-1], interval[-1])]
print Ans
