#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subsets/

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1, 2, 3]

# Output: [[],[0]]
# nums = [0]


def RecursiveSubset(grab, length, startIndex, result, Seen):
    if startIndex == length and tuple(grab) not in Seen:
        Seen.add(tuple(grab))
    for i in range(startIndex, length):
        grab[i] = True
        RecursiveSubset(grab, length, i+1, result, Seen)
        grab[i] = False
        RecursiveSubset(grab, length, i+1, result, Seen)


length = len(nums)
grab = [False] * length
Seen = set()
RecursiveSubset(grab, length, 0, [], Seen)
Ans = [[] for _ in range(len(Seen))]
for i, row in enumerate(Seen):
    for j, doGrab in enumerate(row):
        if doGrab:
            Ans[i].append(nums[j])
print Ans
