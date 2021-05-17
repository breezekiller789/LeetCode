#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/meeting-rooms/

intervals = [
    [0, 30],
    [5, 10],
    [15, 20]
]
intervals = [[7,10],[2,4]]
intervals = sorted(intervals)
for idx, interval in enumerate(intervals[1:], start=1):
    if interval[0] < intervals[idx-1][-1]:
        print False
        exit()
print True
