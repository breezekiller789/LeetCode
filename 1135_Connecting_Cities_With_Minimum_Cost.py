#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq

# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

# Output: 6
# Explanation:
# Choosing any 2 edges will connect all cities so we choose the minimum 2.
n = 3
connections = [
    [1, 2, 5],
    [1, 3, 6],
    [2, 3, 1]
]

# Output: -1
# Explanation:
# There is no way to connect all cities even if all edges are used.
n = 4
connections = [
    [1, 2, 3],
    [3, 4, 4]
]

# Output: 6
n = 4
connections = [
    [1, 2, 1],
    [1, 3, 2],
    [3, 4, 4],
    [1, 4, 3]
]

# Output: 166998
n = 5
connections = [
    [2, 1, 50459],
    [3, 2, 47477],
    [4, 2, 52585],
    [5, 3, 16477]
]


def union(Parents, source, target):
    parent1 = find(Parents, source)
    parent2 = find(Parents, target)
    Parents[parent1] = parent2


def find(Parents, target):
    if Parents[target] != target:
        Parents[target] = find(Parents, Parents[target])
    return Parents[target]


graph = [[0 for _ in range(n)] for _ in range(n)]
for source, target, weight in connections:
    graph[source-1][target-1] = weight

Parents = [_ for _ in range(n)]
# connections.sort(key=lambda x: x[2])
heap = [[weight, source-1, target-1] for source, target, weight in connections]
heapq.heapify(heap)

totalCost = 0
while heap:
    weight, source, target = heapq.heappop(heap)
    if find(Parents, source) != find(Parents, target):
        union(Parents, source, target)
        totalCost += weight
Components = set()
for i in range(n):
    Components.add(find(Parents, i))
print totalCost if len(Components) == 1 else -1
