#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/employee-free-time/

# 這一題基本上就是Question 56，Merge Intervals。

schedule = [
    [[1, 2], [5, 6]],
    [[1, 3]],
    [[4, 10]]
]
schedule = [
    [[1, 3], [6, 7]],
    [[2, 4]],
    [[2, 5], [9, 12]]
]

Intervals = []
for peopleSchedule in schedule:
    for interval in peopleSchedule:
        Intervals.append(interval)
Intervals.sort()
ValidInterval = []
for i, interval in enumerate(Intervals):
    if not ValidInterval or interval[0] > ValidInterval[-1][-1]:
        ValidInterval.append(interval)
    else:
        ValidInterval[-1] = [ValidInterval[-1][0],
                             max(ValidInterval[-1][-1], interval[1])]
availableInterval = []
for i, interval in enumerate(ValidInterval[:-1]):
    availableInterval.append([interval[1], ValidInterval[i+1][0]])
print availableInterval
