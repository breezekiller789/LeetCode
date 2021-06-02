#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/unique-binary-search-trees/

# 這一題竟然是Catalan number
# (2n n) / (n+1)

# Output: 5
n = 3

# Output: 1
# n = 1


def Factorial(num):
    Total = 1
    count = 1
    while count <= num:
        Total *= count
        count += 1
    return Total


print (Factorial(2*n)/(Factorial(n)**2))/(n+1)
