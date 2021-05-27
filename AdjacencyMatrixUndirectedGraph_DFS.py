#!/usr/bin/env python3
# -*- coding: utf-8 -*-


graph = [
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
]


# Iterative
def DFS(graph, Visited, start):
    Stack = [start]
    while Stack:
        currentNode = Stack.pop()
        print currentNode
        Visited.add(currentNode)
        for neighbor in range(len(graph[currentNode])):
            if graph[currentNode][neighbor] == 1 and neighbor not in Visited:
                Stack.append(neighbor)


Visited = set()
for i, row in enumerate(graph):
    for j, num in enumerate(row):
        if num == 1 and i not in Visited:
            DFS(graph, Visited, i)


# Recursion
# def DFS(graph, Visited, node):
#     print node, " "
#     Visited.add(node)
#     for i in range(len(graph[node])):
#         if graph[node][i] == 1 and i not in Visited:
#             DFS(graph, Visited, i)


# Visited = set()
# for i, row in enumerate(graph):
#     for j, num in enumerate(row):
#         if num == 1 and i not in Visited:
#             DFS(graph, Visited, i)
