#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/add-digits/

# 1. num = Added_Number(num)
# 2. while isTwoDigits(num):
# 3.    num = Added_Number(num)

# Added_Number(num):
#     Sum = 0
#     for char in str(num):
#         Sum += int(char)
#     return Sum

# isTwoDigits(num):
#     return len(str(num)) >= 2


# ============Code=============


def Added_Number(num):
    Sum = 0
    for char in str(num):
        Sum += int(char)
    return Sum


def isTwoDigits(num):
    return len(str(num)) >= 2


num = 889
num = Added_Number(num)
while isTwoDigits(num):
    num = Added_Number(num)
print num
