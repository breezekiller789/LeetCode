#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/diagonal-traverse/

# 1. I implement this using BFS because the way it shows the elements is very
# similar to the BFS algorithm, that gave the idea of using BFS.
# 2. I also implement it layer by layer, kinda like n-ary tree level order
# traversal, that way, i can reverse certain layer by pushing it to the stack.

# Define "Neighbors"
#     X
#    X1X
#     X

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def UpdateNeighbors(mat, dataStructure, center, Visited):
    x, y = center

    # Up neighbor
    if x >= 1 and y < Col and (x-1, y) not in Visited:
        dataStructure.append((x-1, y))
        Visited.add((x-1, y))

    # Right neighbor
    if x < Row and y < Col-1 and (x, y+1) not in Visited:
        dataStructure.append((x, y+1))
        Visited.add((x, y+1))

    # Down neighbor
    if x < Row-1 and y < Col and (x+1, y) not in Visited:
        dataStructure.append((x+1, y))
        Visited.add((x+1, y))

    # Left neighbor
    if x < Row and y >= 1 and (x, y-1) not in Visited:
        dataStructure.append((x, y-1))
        Visited.add((x, y-1))


Stack = []
Queue = [(0, 0)]
Ans = []
roundCount = 0
Visited = {(0, 0)}
Row = len(mat)
Col = len(mat[0])
while Queue:
    nextLevelCount = len(Queue)
    while nextLevelCount > 0:
        x, y = Queue[0]
        del Queue[0]
        Visited.add((x, y))
        if roundCount % 2 == 0:
            Stack.append(mat[x][y])
        else:
            Ans.append(mat[x][y])
        # print mat[x][y]
        UpdateNeighbors(mat, Queue, (x, y), Visited)
        nextLevelCount -= 1
    while Stack:
        Ans.append(Stack.pop())

    roundCount += 1
print Ans
