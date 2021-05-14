#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/redundant-connection/

# 用disjoint set來解，不難。


def Union(Parents, edge, Redundants):
    node1, node2 = edge
    parent1 = Find(Parents, node1)
    parent2 = Find(Parents, node2)
    if parent1 == parent2:
        Redundants.append([node1, node2])
    Parents[parent2] = parent1


def Find(Parents, node):
    if node != Parents[node]:
        Parents[node] = Find(Parents, Parents[node])
        return Parents[node]
    return Parents[node]


edges = [[1, 2], [1, 3], [2, 3]]     # [2, 3]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]     # [1, 4]


Parents = [i for i in range(len(edges)+1)]
Redundants = []
for edge in edges:
    Union(Parents, edge, Redundants)
    # print Parents, Redundants
print Redundants[-1]
