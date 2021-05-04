#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/the-maze/

# 1. Call BFS
# 2. If cannot find destination, return false
# 3, If find destination, check if destination is surrounded by walls, if true,
# return true, else return false

# =========Code==========


def isSurroundedByWalls(maze, (x, y), Row, Col):
    WallCount = 0
    # Up neighbor
    if x-1 < 0 or maze[x-1][y] == 1:
        WallCount += 1
    # Right neighbor
    if y == Col-1 or maze[x][y+1] == 1:
        WallCount += 1
    # Down neighbor
    if x == Row-1 or maze[x+1][y] == 1:
        WallCount += 1
    # Left neighbor
    if y-1 < 0 or maze[x][y-1] == 1:
        WallCount += 1
    return WallCount == 3


def BFS(maze, start, destination):
    start = tuple(start)
    destination = tuple(destination)
    Q = [start]
    Visited = {start}
    Row = len(maze)
    Col = len(maze[0])
    while Q:
        x, y = Q[0]
        del Q[0]
        if (x, y) == destination:
            return isSurroundedByWalls(maze, (x, y), Row, Col)

        # Up neighbor
        if x >= 1 and y < Col:
            if maze[x-1][y] == 0 and (x-1, y) not in Visited:
                Q.append((x-1, y))
        # Right neighbor
        if x < Row and y < Col-1:
            if maze[x][y+1] == 0 and (x, y+1) not in Visited:
                Q.append((x, y+1))
        # Down neighbor
        if x < Row-1 and y < Col:
            if maze[x+1][y] == 0 and (x+1, y) not in Visited:
                Q.append((x+1, y))
        # Left neighbor
        if x < Row and y >= 1:
            if maze[x][y-1] == 0 and (x, y-1) not in Visited:
                Q.append((x, y-1))
        Visited.add((x, y))


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = [0, 4]
destination = [4, 4]

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = [0, 4]
destination = [3, 2]

maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0]
]
start = [4, 3]
destination = [0, 1]

# maze = [
#     [0, 0, 1, 0, s],
#     [0, 0, d, 0, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0]
# ]
# start = [0, 4]
# destination = [1, 2]
print BFS(maze, start, destination)
