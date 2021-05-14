#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/count-binary-substrings/

# This is definitely not a easy question man...

s = "00110011"
# s = "10101"
length = len(s)
Counts = []
Current = 1
Previous = 0
Ans = 0
for idx in range(1, length):
    if s[idx-1] == s[idx]:
        Current += 1
    else:
        Ans += min(Previous, Current)
        Previous = Current
        Current = 1
print Ans + min(Previous, Current)
