#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/kill-process/


pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

Parent = dict()
for idx, num in enumerate(ppid):
    Parent[num] = Parent.get(num, [])
    Parent[num].append(pid[idx])
Q = [kill]
result = []
while Q:
    currentNode = Q.pop(0)  # Here we also can use pop() instead, makes it stack
    # currentNode = Q.pop()
    result.append(currentNode)
    Q.extend(Parent.get(currentNode, []))
print result
