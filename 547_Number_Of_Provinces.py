#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/number-of-provinces/

# Disjoint Set


def Union(Parents, Key1, Key2):
    Parent1 = Find(Parents, Key1)
    Parent2 = Find(Parents, Key2)
    Parents[Parent2] = Parent1


# Recursively find the root
def Find(Parents, Key):
    if Parents[Key] != Key:
        Parents[Key] = Find(Parents, Parents[Key])
    return Parents[Key]


isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
isConnected = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]
isConnected = [
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]
length = len(isConnected)
Parents = [i for i in range(length)]

# Do Union
for idx, row in enumerate(isConnected):
    for jdx, col in enumerate(row):
        if idx == jdx:
            continue
        if isConnected[idx][jdx] == 1:
            Union(Parents, idx, jdx)

# Get all the parents
HashTable = set()
for idx, parent in enumerate(Parents):
    HashTable.add(Find(Parents, idx))
print len(HashTable)
