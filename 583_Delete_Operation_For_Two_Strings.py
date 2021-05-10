#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/delete-operation-for-two-strings/


def LCS_DP(s1, s2):
    s1Length = len(s1)
    s2Length = len(s2)
    dp = [[None for _ in range(s2Length+1)] for _ in range(s1Length+1)]
    for idx in range(s1Length+1):
        for jdx in range(s2Length+1):
            if idx == 0 or jdx == 0:
                dp[idx][jdx] = 0
            elif s1[idx-1] == s2[jdx-1]:
                dp[idx][jdx] = dp[idx-1][jdx-1] + 1
            else:
                dp[idx][jdx] = max(dp[idx-1][jdx], dp[idx][jdx-1])
    return dp[s1Length][s2Length]


# word1 = "sea"
# word2 = "eat"
word1 = "leetcode"
word2 = "etco"
length = LCS_DP(word1, word2)
print len(word1)-length + len(word2)-length
