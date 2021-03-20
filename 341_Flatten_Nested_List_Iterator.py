#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/flatten-nested-list-iterator/


def Nested(Lists):
    global Ans
    for i in Lists:
        if isinstance(i, list):
            Nested(i)
        else:
            Ans.append(i)


# nums = [[1, 1], 2, [1, 1]]
nums = [1, [4, [6]]]
Ans = []
Nested(nums)
print Ans
