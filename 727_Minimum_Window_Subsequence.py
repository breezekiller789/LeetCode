#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-window-subsequence/

# 我用跟76題很類似的方法做，但是其實需求不太一樣，我有做了一些修改，但是TLE :(

# Output: "bcde"
s1 = "abcdebdde"
s2 = "bde"
s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
s2 = "u"


def StillStatisfy(string, s2):
    index1 = 0
    index2 = 0
    while index1 < len(string) and index2 < len(s2):
        if string[index1] != s2[index2]:
            index1 += 1
        else:
            index1 += 1
            index2 += 1

    if index2 < len(s2):
        return False
    else:
        return True


left = 0
right = 0
Minimum = [float("inf"), None]
currentWindow = dict()
for i, char in enumerate(s1):
    while StillStatisfy(s1[left:right+1], s2):
        if right-left+1 < Minimum[0]:
            Minimum = [right-left+1, (left, right)]
        left += 1
    right += 1

if Minimum[1]:
    start, end = Minimum[1]
    print s1[start:end+1]
else:
    print ""
