#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-path-sum/
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
grid = [
    [1, 2, 3],
    [4, 5, 6]
]
grid = [
    [5, 4, 2, 9, 6, 0, 3, 5, 1, 4, 9, 8, 4, 9, 7, 5, 1],
    [3, 4, 9, 2, 9, 9, 0, 9, 7, 9, 4, 7, 8, 4, 4, 5, 8],
    [6, 1, 8, 9, 8, 0, 3, 7, 0, 9, 8, 7, 4, 9, 2, 0, 1],
    [4, 0, 0, 5, 1, 7, 4, 7, 6, 4, 1, 0, 1, 0, 6, 2, 8],
    [7, 2, 0, 2, 9, 3, 4, 7, 0, 8, 9, 5, 9, 0, 1, 1, 0],
    [8, 2, 9, 4, 9, 7, 9, 3, 7, 0, 3, 6, 5, 3, 5, 9, 6],
    [8, 9, 9, 2, 6, 1, 2, 5, 8, 3, 7, 0, 4, 9, 8, 8, 8],
    [5, 8, 5, 4, 1, 5, 6, 6, 3, 3, 1, 8, 3, 9, 6, 4, 8],
    [0, 2, 2, 3, 0, 2, 6, 7, 2, 3, 7, 3, 1, 5, 8, 1, 3],
    [4, 4, 0, 2, 0, 3, 8, 4, 1, 3, 3, 0, 7, 4, 2, 9, 8],
    [5, 9, 0, 4, 7, 5, 7, 6, 0, 8, 3, 0, 0, 6, 6, 6, 8],
    [0, 7, 1, 8, 3, 5, 1, 8, 7, 0, 2, 9, 2, 2, 7, 1, 5],
    [1, 0, 0, 0, 6, 2, 0, 0, 2, 2, 8, 0, 9, 7, 0, 8, 0],
    [1, 1, 7, 2, 9, 6, 5, 4, 8, 7, 8, 5, 0, 3, 8, 1, 5],
    [8, 9, 7, 8, 1, 1, 3, 0, 1, 2, 9, 4, 0, 1, 5, 3, 1],
    [9, 2, 7, 4, 8, 7, 3, 9, 2, 4, 2, 2, 7, 8, 2, 6, 7],
    [3, 8, 1, 6, 0, 4, 8, 9, 8, 0, 2, 5, 3, 5, 5, 7, 5],
    [1, 8, 2, 5, 7, 7, 1, 9, 9, 8, 9, 2, 4, 9, 5, 4, 0],
    [3, 4, 4, 1, 5, 3, 3, 8, 8, 6, 3, 5, 3, 8, 7, 1, 3]
]


# DP解法，beats 92.71%，想法還真簡單...我把他想太複雜。
m = len(grid)
n = len(grid[0])
dp = [[float("inf") for _ in range(n)] for _ in range(m)]
dp[0][0] = grid[0][0]

# 先把第零列都先加好，因為我們只能往右往下走，不能往上往左走，所以第零列可以直接
# 都加好。
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]
# 跟列一樣，這個只是先把第零行都先加好。
for i in range(1, m):
    dp[i][0] = dp[i-1][0] + grid[i][0]

for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            continue
        else:
            # 這個就是在做relax
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
print dp[-1][-1]


# My Dijkstra solution, got TLE:((
# def UpdateNeighbors(grid, currentNode, Distance, Q, m, n, Visited):
#     x, y = currentNode
#     # Right neighbor
#     if x < m and y < n-1 and (x, y+1) not in Visited:
#         Q.append((x, y+1))
#         Relax(grid, currentNode, (x, y+1), Distance)
#     # Down neighbor
#     if x < m-1 and y < n and (x+1, y) not in Visited:
#         Q.append((x+1, y))
#         Relax(grid, currentNode, (x+1, y), Distance)


# def Relax(grid, currentNode, nodeToRelax, Distance):
#     x, y = currentNode
#     Relax_X, Relax_Y = nodeToRelax
#     tmpDistance = Distance[(x, y)] + grid[Relax_X][Relax_Y]
#     # Enter this if found a shorter path, do relax
#     if tmpDistance < Distance[(Relax_X, Relax_Y)]:
#         Distance[(Relax_X, Relax_Y)] = tmpDistance


# def ExtraceMin(Q, Distance, Visited):
#     Min = float("inf")
#     ret = None
#     for node in Distance:
#         if Distance[node] < Min and node not in Visited:
#             Min = Distance[node]
#             ret = node
#     return ret


# Start = (0, 0)
# Visited = set(Start)
# m = len(grid)
# n = len(grid[0])
# Distance = {Start: grid[0][0]}
# Q = []
# for i, row in enumerate(grid):
#     for j, cost in enumerate(row):
#         if (i, j) == Start:
#             continue
#         Distance[(i, j)] = float("inf")

# UpdateNeighbors(grid, Start, Distance, Q, m, n, Visited)
# while Q:
#     currentNode = ExtraceMin(Q, Distance, Visited)
#     if not currentNode:
#         break

#     # Update the start node's neighbors
#     UpdateNeighbors(grid, currentNode, Distance, Q, m, n, Visited)
#     Visited.add(currentNode)
# print Distance[(m-1, n-1)]
