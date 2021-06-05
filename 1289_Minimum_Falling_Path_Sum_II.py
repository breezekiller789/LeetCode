#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-falling-path-sum-ii/

# 這一題完全跟265一模一樣，我照抄就AC了，因為題目幾乎就一樣。

# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def RecursivePaint(costs, start, lastColorPicked, totalColors, alreadyChecked):
    # Base case
    if start >= len(costs):
        return 0
    # Base case, 如果是最後一個屋子，就回傳cost最小的，但是顏色不可以跟上個一樣
    elif start == len(costs)-1:
        return min(
            num for i, num in enumerate(costs[-1]) if i != lastColorPicked)
    # 如果現在start剛剛已經算過了，就不用再算一次。
    else:
        minCost = float("inf")
        # 如果alreadyChecked全部都是None，就不用做了，因為全部都還沒算過。
        if not all(cost is None for cost in alreadyChecked[start]):
            return min(num
                       for i, num in enumerate(alreadyChecked[start])
                       if i != lastColorPicked and num is not None)
    minCost = float("inf")
    for currentColorPicked in range(totalColors):
        # 如果顏色跟上一個屋子一樣，那就存這個屋子這個顏色的最小值就好，
        # 不要去跟前面的minCost比，因為這個顏色不可以塗
        if currentColorPicked == lastColorPicked:
            ret = RecursivePaint(
                costs, start+1, currentColorPicked,
                totalColors, alreadyChecked) + costs[start][currentColorPicked]
            alreadyChecked[start][currentColorPicked] = ret
            continue
        # 現在的顏色跟上一個不一樣的話，代表可以塗，那就遞迴算最小cost
        ret = RecursivePaint(
            costs, start+1, currentColorPicked,
            totalColors, alreadyChecked) + costs[start][currentColorPicked]
        minCost = min(minCost, ret)     # 跟目前最小值比看誰小
        alreadyChecked[start][currentColorPicked] = ret     # Memoization
    return minCost


alreadyChecked = [[None for _ in range(len(arr[0]))]
                  for _ in range(len(arr))]
alreadyChecked[-1] = arr[-1]
totalColors = len(arr[0])
print RecursivePaint(arr, 0, None, totalColors, alreadyChecked)
