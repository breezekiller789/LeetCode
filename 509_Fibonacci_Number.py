#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/fibonacci-number/


def fib(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n-1) + fib(n-2)
        return dp[n]


n = 30

if n == 0 or n == 1:
    print n
    exit()
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1

print fib(n)
