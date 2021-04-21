#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue

# https://leetcode.com/problems/walls-and-gates/

# 1. for each gate, call BFS, update all empty room's distance, if
# current_Distance is less than node_Distance, update it to the current


# =========Code==========


def isEmptyRoom(i, j):
    return rooms[i][j] != -1 and rooms[i][j] != 0


def Update_Neighbors(x, y, dist, Visited, Q):
    # UP Neighbor
    if x-1 >= 0:
        if isEmptyRoom(x-1, y) and [x-1, y] not in Visited:
            Q.put((x-1, y, dist+1))
            Visited.append([x-1, y])
            if dist+1 < rooms[x-1][y]:
                rooms[x-1][y] = dist+1
    # Right Neighbor
    if y+1 < len(rooms[0]):
        if isEmptyRoom(x, y+1) and [x, y+1] not in Visited:
            Q.put((x, y+1, dist+1))
            Visited.append([x, y+1])
            if dist+1 < rooms[x][y+1]:
                rooms[x][y+1] = dist+1
    # Down Neighbor
    if x+1 < len(rooms):
        if isEmptyRoom(x+1, y) and [x+1, y] not in Visited:
            Q.put((x+1, y, dist+1))
            Visited.append([x+1, y])
            if dist+1 < rooms[x+1][y]:
                rooms[x+1][y] = dist+1
    # Left Neighbor
    if y-1 >= 0:
        if isEmptyRoom(x, y-1) and [x, y-1] not in Visited:
            Q.put((x, y-1, dist+1))
            Visited.append([x, y-1])
            if dist+1 < rooms[x][y-1]:
                rooms[x][y-1] = dist+1
    return Visited


def BFS(i, j):
    Q = queue.Queue()
    Q.put((i, j, 0))
    Visited = [[i, j]]
    while not Q.empty():
        x, y, dist = Q.get()
        Visited = Update_Neighbors(x, y, dist, Visited, Q)


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

for i, row in enumerate(rooms):
    for j, element in enumerate(row):
        if element == 0:
            BFS(i, j)
print rooms
