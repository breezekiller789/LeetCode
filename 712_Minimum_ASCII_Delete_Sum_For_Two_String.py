#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


def LCS(s1, s2):
    s1Length = len(s1)
    s2Length = len(s2)
    dp = [[None for _ in range(s2Length+1)] for _ in range(s1Length+1)]
    for i in range(s1Length+1):
        for j in range(s2Length+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[s1Length][s2Length]


# 231 = 115(s) + 116(t)
s1 = "sea"
s2 = "eat"

# 403 = 100(d)+101(e)+101(e)+101(e)
s1 = "delete"
s2 = "leet"


# [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 1, 1, 1],
#     [0, 1, 2, 2]
# ]
print LCS(s1, s2)
