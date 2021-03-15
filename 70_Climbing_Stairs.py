#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/climbing-stairs/

# 1 . get # of 2's
# 2 . use that as loop condition, decrement # of 2 by 1, increment # of 1 by 2
# 3 . calculate the equation of permutations which is
# 4 .      (m+k)!
#        ---------
#          m!*k!


def Factorial(num):
    Sum = 1
    for i in range(1, num+1):
        Sum *= i
    return Sum


def Permutations(m, k):
    return Factorial(m+k) / (Factorial(m) * Factorial(k))


def Climb(num_2, n):
    Count = 0
    while num_2 >= 0:
        num_1 = n - num_2 * 2
        # print num_1, num_2, Permutations(num_1, num_2)
        Count += Permutations(num_1, num_2)
        num_2 -= 1
    return Count


n = 4
print Climb(n/2, n)
