#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sparse-matrix-multiplication/

# 1. for each multiplication, check if there is 0 for multiplier and
# multiplicant, if anyone of them is 0, skip this multiplication
# 2. Matrix multiplication formula: Cij = ∑ Aik*Bkj, Ref Linear Algebra

# =======Code=========

mat1 = [
    [1, 0, 0],
    [-1, 0, 3]
]
mat2 = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
# mat1 = [[1, -5]]
# mat2 = [[12], [-1]]

Rows = len(mat1)            # Get the m of final matrix
Cols = len(mat2[0])         # Get the n of final matrix
mat1_Cols = len(mat1[0])    # Get the colums of A or rows of B, works the same
Ans = [[] for i in range(Rows)]

for i in range(Rows):
    for j in range(Cols):
        Sum = 0
        for k in range(mat1_Cols):
            if mat1[i][k] == 0 or mat2[k][j] == 0:
                continue
            Sum += mat1[i][k]*mat2[k][j]
        Ans[i].append(Sum)
print Ans
