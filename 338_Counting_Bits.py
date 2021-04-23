#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/counting-bits/

# 1. Calculate every binary representation within 0~n
# 2. Count 1 in binary representation

# =========Code==========

num = 1022

# Method 1, my first thought
# def Decimal_To_Binary(n):
#     oneCount = 0
#     while n / 2:
#         if n % 2 == 1:
#             oneCount += 1
#         n /= 2
#     if n % 2 == 1:
#         oneCount += 1
#     return oneCount


# oneList = []

# for n in range(num+1):
#     oneList.append(Decimal_To_Binary(n))
# print oneList

# Method 2, using built-in function bin(), 50%
# oneList = []
# for n in range(num+1):
#     oneList.append(bin(n).count("1"))
# print oneList

# Method 3. Fastest way to do this, Using DP + Least Significant Bit operation,
# for example, 605 = 1001011101, 302 = 100101110, 302 is 605 removing LSB,
# 605 = 302*2 + 1. To sum up, the equation will look like
# P(x) = P(x/2) + (x % 2)

oneList = [0 for i in range(num+1)]
for n in range(num+1):
    oneList[n] = oneList[n>>1] + (n & 1)
print oneList
