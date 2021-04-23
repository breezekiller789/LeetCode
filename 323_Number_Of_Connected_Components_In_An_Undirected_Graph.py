#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# 1. Use Disjoin Set (Union, Find)

# ========Code============


def Union(edge1, edge2, Parents):
    parent1 = Find(edge1, Parents)
    parent2 = Find(edge2, Parents)
    Parents[parent1] = parent2


def Find(edge, Parents):
    if Parents[edge] != edge:
        Parents[edge] = Find(Parents[edge], Parents)
    return Parents[edge]


n = 5
edges = [[0, 1]]
n = 5
edges = [
    [0, 1],
    [1, 2],
    [3, 4]
]
# n = 5
# edges = [
#     [0, 1],
#     [1, 2],
#     [2, 3],
#     [3, 4]
# ]

# n = 4
# edges = [
#     [2, 3],
#     [1, 2],
#     [1, 3]
# ]
# n = 5
# edges = [[0, 1], [1, 2], [3, 4]]

# indicates each node's parent, for example, Parents[0] = 2, it means that node
# 0's parent is node 2
Parents = [i for i in range(n)]

# Union all edges
for edge in edges:
    Union(edge[0], edge[1], Parents)

Subsets = set()
# go through every node, find it's parent and add it to the set, set won't count
# same element twice
for idx in range(n):
    Subsets.add(Find(idx, Parents))
print len(Subsets)
