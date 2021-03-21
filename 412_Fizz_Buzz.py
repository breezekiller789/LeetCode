#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/fizz-buzz/

# 很簡單

n = 15

# ============Code Starts===========

Ans = []
for i in range(1, n+1):
    if i % 15 == 0:     # 注意最小公倍數。
        Ans.append("FizzBuzz")
    if i % 3 == 0:
        Ans.append("Fizz")
    elif i % 5 == 0:
        Ans.append("Buzz")
    else:
        Ans.append(str(i))
print Ans
