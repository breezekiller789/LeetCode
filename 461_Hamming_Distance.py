#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/hamming-distance/

# 1. XOR to show the distance
# 2. then count 1's in this binary representation

# ========Code========


def Count1s(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count


x = 7
y = 8

x ^= y
print Count1s(x)
