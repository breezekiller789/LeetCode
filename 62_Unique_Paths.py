#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/unique-paths/

# 離散數學排列組合有教過了，就算出往右走幾步，往下走幾步，加起來算階乘，除以重複
# 例如：往下兩步，往右四步，算起來就像下面這樣。
#  (2+4)!
# --------
#  2!*4!


def factorial(fac):
    Sum = 1
    for i in range(1, fac+1):
        Sum *= i
    return Sum


m, n = 3, 7

# 先算階乘
# 這邊都要減一的原因是因為三個格子，能夠走的就是兩步
print factorial((m-1)+(n-1)) / (factorial(m-1) * factorial(n-1))
