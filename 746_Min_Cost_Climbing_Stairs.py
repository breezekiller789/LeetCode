#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/min-cost-climbing-stairs/

cost = [10, 15, 20]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [0, 0, 0, 0, 1, 1, 1, 1]
# cost = [0, 0, 1, 1]


# 用recursion + memoization
def RecursiveClimb(cost, start, alreadyChecked):
    if start >= len(cost):
        return 0
    elif start == len(cost)-1:
        return cost[-1]
    elif start == len(cost)-2:
        return cost[-2]
    if alreadyChecked[start] is not None:
        return alreadyChecked[start]
    oneStep = RecursiveClimb(cost, start+2, alreadyChecked) + cost[start]
    twoStep = RecursiveClimb(cost, start+1, alreadyChecked) + cost[start]
    alreadyChecked[start] = min(oneStep, twoStep)
    return alreadyChecked[start]


alreadyChecked = [None for _ in range(len(cost))]
print min(RecursiveClimb(cost, 0, alreadyChecked),
          RecursiveClimb(cost, 1, alreadyChecked))

# 用Bottom-up DP比較不直覺
# dp = [0 for _ in range(len(cost))]
# dp[0] = cost[0]
# dp[1] = cost[1]
# if len(cost) < 3:
#     print min(cost[0], cost[1])
#     exit()
# elif len(cost) < 4:
#     print min(cost[0]+cost[2], cost[1])
#     exit()

# for i, currentCost in enumerate(cost[2:], start=2):
#     dp[i] = min(dp[i-1], dp[i-2]) + currentCost

# print min(dp[-1], dp[-2])
