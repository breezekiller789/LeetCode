#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def LevelOrder(root):
    Q = [root]
    Ans = []
    # Q will always keep the node on the same level
    while Q:
        childrenCount = len(Q)  # Number of nodes on the same level
        Ans.append([])
        while childrenCount > 0:
            currentNode = Q[0]
            Q = Q[1:]
            Ans[-1].append(currentNode.val)
            # Put all of next level's node into Q
            for child in currentNode.children:
                Q.append(child)
            childrenCount -= 1
    print Ans


root = Node(1, [])
root.children.extend([Node(3, []), Node(2, []), Node(4, [])])
root.children[0].children.extend([Node(5, []), Node(6, [])])
LevelOrder(root)
