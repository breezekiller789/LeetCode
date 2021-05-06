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


print LCS("appl", "applet")
