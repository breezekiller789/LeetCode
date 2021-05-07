#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/is-subsequence/

# Method 1, LCS but got TLE
# 1. Using the Longest Common Subsequence algorithm to solve this problem

# Method 2, Using DP
# Solution: https://www.youtube.com/watch?v=sSno9rV8Rhg&t=1102s


# Initial Thoughts, doesn't work because this problem is requiring the orders of
# string s should be in order, it cannot be changed.
# 1. Using hashing, first of all, hash all characters in string t, and then
# check string s, if every character in string s is in the hash table, if the
# character is in the hash table, decrement the count of that character, if
# count is less than 0, return false

# =======Code=========
s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s = "acb"
# t = "ahbgdc"
s = "abpcplea"
t = "abpcplaaa"
length_s = len(s)
length_t = len(t)


# Method 1, TLE
# def LCS(i, j, length_s, length_t):
#     if i == length_s or j == length_t:
#         return 0
#     elif s[i] == t[j]:
#         return 1 + LCS(i+1, j+1, length_s, length_t)
#     else:
#         return max(LCS(i+1, j, length_s, length_t),
#                    LCS(i, j+1, length_s, length_t))


# ret = LCS(0, 0, length_s, length_t)
# if ret != length_s:
#     print False
# else:
#     print True


# Method 2, LCS using Dynamic Programming
DP = [[0 for i in range(length_t)] for x in range(length_s)]
print DP
for i, row in enumerate(DP):
    for j, col in enumerate(row):
        if s[i] == t[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print DP
if DP[length_s-1][length_t-1] != length_s:
    print False
else:
    print True
