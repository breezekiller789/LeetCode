#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/combination-sum/

# AC, 但是很慢ＸＤ，因為用遞迴解。

# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
candidates = [2, 3, 6, 7]
target = 7

# Output: [[2,2,2,2],[2,3,3],[3,5]]
candidates = [2, 3, 5]
target = 8

# Output: []
# candidates = [2]
# target = 1

# Output: [[1]]
# candidates = [1]
# target = 1

# Output: [[1,1]]
candidates = [1]
target = 2


def RecursiveCombine(candidates, target, currentPath, result):
    if target < 0:
        return
    if target == 0:
        currentPath.sort()
        if currentPath not in result:
            result.append(currentPath)
    for num in candidates:
        RecursiveCombine(candidates, target-num, currentPath+[num], result)


results = []
RecursiveCombine(candidates, target, [], results)
print results
