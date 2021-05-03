#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/island-perimeter/

# 1. Scan through the whole graph
# 2. If current node is 1, then count all it's neighbors that is also 1
# 3. Substract it with 4, because a sqare has perimeter 4

# ========Code=========

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
Rows = len(grid)
Cols = len(grid[0])
Sum = 0

for i, row in enumerate(grid):
    for j, num in enumerate(row):
        if num == 1:
            # This is island, count all it's neighbors
            neighborIslands = 0

            # Up neighbor
            if i >= 1 and j < Cols:
                if grid[i-1][j]:
                    neighborIslands += 1
            # Right neighbor
            if i < Rows and j < Cols-1:
                if grid[i][j+1]:
                    neighborIslands += 1
            # Down neighbor
            if i < Rows-1 and j < Cols:
                if grid[i+1][j]:
                    neighborIslands += 1
            # Left neighbor
            if i < Rows and j >= 1:
                if grid[i][j-1]:
                    neighborIslands += 1
            Sum += 4-neighborIslands
print Sum
