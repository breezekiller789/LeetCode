#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/nested-list-weight-sum-ii/

# ===========Code==============


def NestedListWeight(nestedList, depth):
    Max = float("-inf")
    for element in nestedList:
        if isinstance(element, list):
            Max = max(Max, NestedListWeight(element, depth+1))
        else:
            Max = max(Max, depth)
    return Max


def WeightSum(nestedList, Depths, depth):
    Sum = 0
    Current_Depth_Max = Depths[depth]
    for element in nestedList:
        if isinstance(element, list):
            Sum += WeightSum(element, Depths, depth+1)
        else:
            Sum += element*Current_Depth_Max
    return Sum


nestedList = [[1, 1], 2, [1, 1]]
nestedList = [1, [4, [6]]]
nestedList = [[], [], []]

Max_Depth = NestedListWeight(nestedList, 1)
if Max_Depth == float("-inf"):
    print 0
    exit()
Depths = [x for x in range(1, Max_Depth+1)]
Depths = Depths[::-1]

print WeightSum(nestedList, Depths, 0)
