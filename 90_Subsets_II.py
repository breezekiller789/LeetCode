#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subsets-ii/

# 跟Q.78類似

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1, 2, 3]

# Output: [[],[0]]
# nums = [0]

# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# [[1, 2], [2, 2], [1], [2], [1, 2], [], [1, 2, 2], [2]]
nums = [1, 2, 2]


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
# Ans = [[] for _ in range(len(Seen))]
Ans = set()
for i, row in enumerate(Seen):
    tmpList = [nums[j] for j, doGrab in enumerate(row) if doGrab]
    # 這邊要做一下排序，因為可能會出現[1, 4], [4, 1]，這些要算一種。
    Ans.add(tuple(sorted(tmpList)))
print [list(_) for _ in Ans]
