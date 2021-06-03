#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/paint-house-ii/

# Output: 5
# Explanation:
# Paint house 0 into color 0, paint house 1 into color 2.
# Minimum cost: 1 + 4 = 5;
# Or paint house 0 into color 2, paint house 1 into color 0.
# Minimum cost: 3 + 2 = 5
costs = [
    [1, 5, 3],
    [2, 9, 4]
]

# Output: 5
# costs = [
#     [1, 3],
#     [2, 4]
# ]

# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house
# 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10
costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]

# Output: 2
costs = [
    [7, 6, 2]
]

# Output: 26
# costs = [
#     [3, 5, 3],
#     [6, 17, 6],
#     [7, 13, 18],
#     [9, 10, 18]
# ]

# Output: 55
costs = [
    [13, 8, 17],
    [6, 8, 19],
    [5, 1, 7],
    [5, 18, 2],
    [12, 3, 4],
    [12, 7, 10],
    [14, 16, 7],
    [19, 17, 19]
]

# Output: 17
costs = [
    [7, 19, 11, 3, 7, 15, 17, 5, 6, 18, 1, 15, 18, 11],
    [13, 18, 18, 8, 13, 12, 11, 13, 4, 8, 2, 4, 5, 20],
    [14, 5, 18, 4, 7, 6, 1, 6, 11, 6, 16, 6, 13, 17],
    [18, 17, 11, 3, 12, 4, 8, 6, 2, 7, 10, 9, 19, 3],
    [4, 3, 2, 14, 11, 15, 18, 1, 17, 1, 6, 14, 14, 9],
    [9, 13, 15, 14, 5, 1, 1, 6, 11, 15, 16, 12, 10, 18],
    [19, 2, 11, 3, 13, 4, 13, 7, 16, 16, 20, 18, 20, 8],
    [8, 19, 20, 9, 18, 13, 17, 1, 2, 4, 3, 20, 15, 9],
    [9, 10, 11, 6, 14, 20, 4, 1, 5, 15, 13, 10, 13, 5],
    [13, 11, 9, 11, 9, 16, 3, 19, 1, 11, 6, 7, 12, 13],
    [14, 1, 15, 14, 11, 12, 7, 14, 12, 11, 6, 9, 5, 5]
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


alreadyChecked = [[None for _ in range(len(costs[0]))]
                  for _ in range(len(costs))]
alreadyChecked[-1] = costs[-1]
totalColors = len(costs[0])
print RecursivePaint(costs, 0, None, totalColors, alreadyChecked)
