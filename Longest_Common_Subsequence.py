#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Finding the longest common subsequence

# Recursion


def LCS(s1, s2):
    if not s1 or not s2:
        return 0
    elif s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    else:
        return max(LCS(s1[1:], s2), LCS(s1, s2[1:]))


def LCS_DP(s1, s2):
    lens1 = len(s1)
    lens2 = len(s2)
    dp = [[None] * (lens2+1) for i in range(lens1+1)]
    i = 0
    while i < lens1+1:
        j = 0
        while j < lens2+1:
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            j += 1
        i += 1
    return dp[lens1][lens2]


print LCS_DP("applet", "appl")
