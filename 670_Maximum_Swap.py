#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-swap/

# I just brute forced it... and it still got an AC


def swap(string, i, j):
    tmp = string[i]
    string[i] = string[j]
    string[j] = tmp
    return int("".join(string))


num = 2736
num = 9973
num = 98368
# num = 1993

string = list(str(num))
length = len(string)
Max = num
for idx in range(length):
    for jdx in range(idx+1, length):
        tmp = swap(string, idx, jdx)
        swap(string, idx, jdx)
        Max = max(Max, tmp)
print Max
