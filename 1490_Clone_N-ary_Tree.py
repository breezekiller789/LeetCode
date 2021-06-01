#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/clone-n-ary-tree/


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def __init__(self):
        self.haha = 0

    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.haha = 0

        def LevelOrder(root):
            if not root:
                return
            newRoot = Node(root.val)
            Q = [(root, newRoot)]
            while Q:
                childCount = len(Q)
                while childCount > 0:
                    currentNode, newCurrentNode = Q.pop(0)
                    for child in currentNode.children:
                        newNode = Node(child.val)
                        Q.append((child, newNode))
                        newCurrentNode.children.append(newNode)
                    childCount -= 1
            return newRoot
        return LevelOrder(root)
