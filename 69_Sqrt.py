#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/sqrtx/

x = 17

# ============Code Starts=============

i = 1
while i * i < x:
    i += 1
if i * i == x:
    print i
else:
    print i-1
