#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/pascals-triangle/

# 其實就只是排列組合當中的排列，也就是C，C 10取3那個C，階乘可以消掉，可以加速很
# 多，剩下的就只是迴圈去控制，離散中的二項式定理(1+x)^n


def Combination(n, k):
    molecular = 1       # 分子
    denominator = 1     # 分母
    # C 10取8等於 C 10取2，但為了要快，越小越好。
    if k > n/2:
        k = n - k
    # 算分子
    for i in xrange(n, n-k, -1):
        molecular *= i
    # 算分母
    for i in range(1, k+1):
        denominator *= i
    return molecular / denominator


rowIndex = 3
for i in range(rowIndex+1):
    print Combination(rowIndex, i)
