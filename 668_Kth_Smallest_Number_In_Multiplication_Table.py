#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


m = 3
n = 3
k = 5
m = 2
n = 3
k = 6


# My initial thought, got TLE
# nums = []
# for idx in range(1, m+1):
#     for jdx in range(1, n+1):
#         nums.append(idx*jdx)
# nums.sort()
# print nums[k-1]
