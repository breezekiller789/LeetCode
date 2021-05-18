#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/network-delay-time/


def GetAdjMatrix(times, n):
    # Transfor times array to a adjacency matrix
    adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
    for start, end, weight in times:
        adjMatrix[start-1][end-1] = weight
    return adjMatrix


def ExtractMin(Distances, Visited):
    # Get the minimum distance from Distances
    Min = [float("inf"), None]
    for idx, num in enumerate(Distances):
        if idx not in Visited and num < Min[0]:
            Min = num, idx
    return Min[1]


def UpdateNeighbors(adjacencyMatrix, Q, Visited, Distances, currentNode, n):
    # Update all neighbor's distance, do relaxing and put neighbors into Q
    for neighbor in range(n):
        if adjacencyMatrix[currentNode][neighbor] != 0:
            Q.append(neighbor)
            Relax(adjacencyMatrix, currentNode, neighbor, Distances)


def Relax(adjacencyMatrix, start, target, Distances):
    # Relax the edges that has shorter path
    Distances[target] = min(Distances[target],
                            Distances[start]+adjacencyMatrix[start][target])


times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]
n = 4
k = 2

# Test case 1
times = [
    [1,2,1]
]
n = 2
k = 1

# Test case 2
times = [
    [1,2,1]
]
n = 2
k = 2

Visited = set()
Distances = [float("inf") for i in range(n)]
Distances[k-1] = 0
adjacencyMatrix = GetAdjMatrix(times, n)
Q = [k-1]
while Q:
    currentNode = ExtractMin(Distances, Visited)
    Visited.add(currentNode)
    if currentNode is None:
        break
    UpdateNeighbors(adjacencyMatrix, Q, Visited, Distances, currentNode, n)
Max = max(Distances)
print Max if Max != float("inf") else -1
# [
#     [0, 0, 0, 0],
#     [1, 0, 1, 0],
#     [0, 0, 0, 1],
#     [0, 0, 0, 0]
# ]
