#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-palindromic-subsequence/

s = "bbbab"
# s = "cbbd"

# Method 1, using recursion, got TLE
# def LPS(s, start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     elif s[start] == s[end]:
#         return 2 + LPS(s, start+1, end-1)

#     return max(LPS(s, start+1, end), LPS(s, start, end-1))

# print LPS(s, 0, len(s)-1)


# Method 2, using DP to speed it up
# Trace the test case of "bbbab"
# dp[4][4] = 1
# dp[3][3] = 1
# dp[3][4] = max(dp[4][4], dp[3][3]) = 1
# dp[2][2] = 1
# dp[2][3] = max(dp[3][3], dp[2][2]) = 1
# dp[2][4] = dp[3][3] + 2 = 3
# dp[1][1] = 1
# dp[1][2] = dp[2][1] + 2 = 2
# dp[1][3] = max(dp[2][3], dp[1][2]) = 2
# dp[1][4] = dp[2][3] + 2 = 1 + 2 = 3
# dp[0][0] = 1
# dp[0][1] = dp[1][0] + 2 = 0 + 2 = 2
# dp[0][2] = dp[1][1] + 2 = 3
# dp[0][3] = max(dp[1][3], dp[0][2]) = 3
# dp[0][4] = dp[1][3] + 2 = 4
length = len(s)
dp = [[0 for _ in range(length)] for _ in range(length)]
for i in xrange(length-1, -1, -1):
    dp[i][i] = 1
    for j in range(i+1, length):
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] + 2
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
print dp[0][length-1]
