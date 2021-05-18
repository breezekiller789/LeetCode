#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/min-cost-climbing-stairs/

cost = [10, 15, 20]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [0, 0, 0, 0, 1, 1, 1, 1]
# cost = [0, 0, 1, 1]
dp = [0 for _ in range(len(cost))]
dp[0] = cost[0]
dp[1] = cost[1]
if len(cost) < 3:
    print min(cost[0], cost[1])
    exit()
elif len(cost) < 4:
    print min(cost[0]+cost[2], cost[1])
    exit()

for i, currentCost in enumerate(cost[2:], start=2):
    dp[i] = min(dp[i-1], dp[i-2]) + currentCost

print min(dp[-1], dp[-2])
