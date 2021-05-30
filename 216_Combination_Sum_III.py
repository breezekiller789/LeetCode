#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/combination-sum-iii/

# 跟39, 40很像，都是用遞迴解。

# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# k = 3
# n = 7

# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# k = 3
# n = 9

# Output: []
# Explanation: There are no valid combinations. [1,2,1] is not valid because 1
# is used twice.
# k = 4
# n = 1

# Output: []
# Explanation: There are no valid combinations.
# k = 3
# n = 2

# Output: [[1,2,3,4,5,6,7,8,9]]
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
# There are no other valid combinations.
k = 9
n = 45


def RecursiveCombine(nums, currentPath, result, k, target, alreadyPicked,
                     startIndex):
    if k == 0 and target == 0:
        result.append(currentPath)
    for i, num in enumerate(nums[startIndex:], start=startIndex):
        if not alreadyPicked[i]:
            alreadyPicked[i] = True
            RecursiveCombine(nums, currentPath+[num], result, k-1, target-num,
                             alreadyPicked, i+1)
            alreadyPicked[i] = False


nums = [i for i in range(1, 10)]
result = []
alreadyPicked = [False for _ in range(9)]
RecursiveCombine(nums, [], result, k, n, alreadyPicked, 0)
print result
