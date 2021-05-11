#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/palindromic-substrings/

# This problem can be solved by DP, but i saw a solution on youtube... this is
# so much easy to understand and straight forward!!
# So, basicly the idea is, a big palindrome is build on top of a smaller
# palindrome, for example, "abcba" is built on top of "bcb", on top of "c", so,
# we only have to expand towards both sides, that's what Count() is doing.

# https://www.youtube.com/watch?v=gI1771HyXu0


def Count(string, start, end, Ans):
    # Expand towards both sides if start and end is identical
    while start >= 0 and end < len(string) and string[start] == string[end]:
        start -= 1  # Move start backwards
        end += 1    # Move end forward
        Ans += 1
    return Ans


s = "abc"   # return 3, [a, b, c]
# s = "aaa"   # return 6, [a, a, a, aa, aa, aaa]

Ans = 0
for idx in range(len(s)):
    Ans = Count(s, idx, idx, Ans)
    Ans = Count(s, idx, idx+1, Ans)
print Ans
