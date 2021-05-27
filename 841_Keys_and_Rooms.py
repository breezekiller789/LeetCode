#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/keys-and-rooms/

# Transform rooms to adjacency matrix
# Apply DFS
# Check if all nodes are visited


# Output: true
# Explanation:
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.
rooms = [
    [1],
    [2],
    [3],
    []
]

# Output: false
# Explanation: We can't enter the room with number 2.
rooms = [
    [1, 3],
    [3, 0, 1],
    [2],
    [0]
]


def DFS(adjMatrix, Visited, startNode):
    stack = [startNode]
    while stack:
        currentNode = stack.pop()
        Visited[currentNode] = True
        for neighbor in range(len(adjMatrix[currentNode])):
            if adjMatrix[currentNode][neighbor] == 1 and not Visited[neighbor]:
                stack.append(neighbor)


def GraphToAdjacencyMatrix(rooms, length):
    adjMatrix = [[0 for _ in range(length)] for _ in range(length)]
    for i, room in enumerate(rooms):
        for num in room:
            if i == num:
                continue
            adjMatrix[i][num] = 1
    return adjMatrix


length = len(rooms)
adjMatrix = GraphToAdjacencyMatrix(rooms, length)
Visited = [False] * length
for i, row in enumerate(adjMatrix):
    for j, num in enumerate(row):
        if num == 1 and not Visited[i]:
            DFS(adjMatrix, Visited, i)
print False not in Visited
