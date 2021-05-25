#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/all-paths-from-source-to-target/

# 用BFS解

# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
graph = [
    [1, 2],
    [3],
    [3],
    []
]

# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
graph = [
    [4, 3, 1],
    [3, 2, 4],
    [3],
    [4],
    []
]

# Output: [[0,1]]
graph = [
    [1],
    []
]

# Output: [[0,1,2,3],[0,2,3],[0,3]]
graph = [
    [1, 2, 3],
    [2],
    [3],
    []
]

# Output: [[0,1,2,3],[0,3]]
graph = [
    [1, 3],
    [2],
    [3],
    []
]


def GraphToAdjacency(graph):
    length = len(graph)
    adjMatrix = [[0 for _ in range(length)] for _ in range(length)]
    for i, row in enumerate(graph):
        for j, dest in enumerate(row):
            adjMatrix[i][dest] = 1
    return adjMatrix


def BFS(adjMatrix):
    Q = [[0]]
    target = len(adjMatrix)-1
    result = []
    while Q:
        currentNode = Q.pop(0)
        if currentNode[-1] == target:
            result.append(currentNode)
            continue
        for i, node in enumerate(adjMatrix[currentNode[-1]]):
            if node == 1:
                Q.append(currentNode+[i])
    print result
    return result


adjMatrix = GraphToAdjacency(graph)
result = BFS(adjMatrix)
