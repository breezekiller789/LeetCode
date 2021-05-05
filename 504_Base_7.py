#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/base-7/


def BinaryRepresentation(n):
    String = ""
    while n:
        String += "{}".format(n % 7)
        n /= 7
    return String[::-1]


# num = 100
# num = 23
num = -7
# num = -15

if num > 0:
    print BinaryRepresentation(num)
else:
    String = BinaryRepresentation(abs(num))
    print "-"+String
