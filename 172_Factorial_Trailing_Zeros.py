#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/factorial-trailing-zeroes/

# 離散的數論就有教了...我的天啊～

n = 5


# ==========Code Starts===========

Count = 0
i = 5
while n / i != 0:
    Count += (n/i)
    i *= 5
print Count
