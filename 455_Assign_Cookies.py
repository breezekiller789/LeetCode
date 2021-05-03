#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/assign-cookies/

g = [1, 2, 3]
s = [1, 1]
# g = [1, 2]
# s = [1, 2, 3]
g = [10, 9, 8, 7]
s = [5, 6, 7, 8]


g.sort()    # Sort child's greed in the first place
s.sort()    # Sort cookies
g_idx = 0
s_idx = 0
g_length = len(g)
s_length = len(s)
count = 0
while g_idx < g_length and s_idx < s_length:
    # Current cookie is sufficient for the greed of current child
    if g[g_idx] <= s[s_idx]:
        count += 1
        g_idx += 1
        s_idx += 1
        continue
    s_idx += 1
print count
