#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/nested-list-weight-sum/

# 1. Use recursion cuz there is a list inside a list.

# ========Code==========


def NestedListWeightSum(nested, depth):
    Sum = 0
    for element in nested:
        if isinstance(element, list):
            Sum += NestedListWeightSum(element, depth+1)
        else:
            Sum += element*depth
    return Sum


nestedList = [[1, 1], 2, [1, 1]]

nestedList = [1, [4, [6]]]
print NestedListWeightSum(nestedList, 1)
