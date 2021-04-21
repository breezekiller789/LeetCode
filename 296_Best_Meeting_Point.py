#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/best-meeting-point/

# 1. 質心公式X(a, b), Y(c, d), Z(e, f) -> ((a+c+e)/3, (b+d+f)/3)


# =========Code==========


def Distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2)+abs(y1-y2)


grid = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0]
]

# grid = [[1, 1]]
Xs = []
Ys = []
for i, row in enumerate(grid):
    for j, point in enumerate(row):
        if point == 1:
            Xs.append(i)
            Ys.append(j)
Xs.sort()
Ys.sort()

centerOfMass_X = Xs[len(Xs)//2]
centerOfMass_Y = Ys[len(Ys)//2]
# print centerOfMass_X, centerOfMass_Y

Sum_Distance = 0
for i, x_position in enumerate(Xs):
    Sum_Distance += Distance((Xs[i], Ys[i]), (centerOfMass_X, centerOfMass_Y))
print Sum_Distance
