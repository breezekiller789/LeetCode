#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/combination-sum-ii/

# 跟Q.39很像

# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

# Output:
# [
# [1,2,2],
# [5]
# ]
# candidates = [2, 5, 2, 1, 2]
# target = 5


def RecursiveCombine(candidates, target, currentPath, result, alreadyPicked,
                     startindex, length):
    if target < 0:
        return
    if target == 0:
        # store result
        currentPath.sort()
        if currentPath not in result:
            result.append(currentPath)
    for i in range(startindex, length):
        # 這一行是重點，少了這一行，會TLE，雖然已經夠慢了，但是這個很關鍵，如果
        # 沒有這一行，遇到[1, 1, 1, 1, 1, 1, 1, 1.....] target = 27這種測資會直接
        # TLE，因為如果我現在這個候選人跟上一個一樣的話，代表說其實他剛剛早就已經
        # 去做過了，我不用再去走他的後程。
        if i > startindex and candidates[i] == candidates[i-1]:
            continue
        if not alreadyPicked[i]:
            alreadyPicked[i] = True
            RecursiveCombine(
                candidates, target-candidates[i], currentPath+[candidates[i]],
                result, alreadyPicked, i+1, length)
            alreadyPicked[i] = False


result = []
currentPath = []
alreadyPicked = [False] * len(candidates)
length = len(candidates)
RecursiveCombine(candidates, target, currentPath, result, alreadyPicked, 0,
                 length)
print result
