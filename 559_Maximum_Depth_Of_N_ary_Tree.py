#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.children = []


def LevelOrder(root):
    Q = [root]
    Level = 0
    while Q:
        numberOfChildren = len(Q)
        while numberOfChildren > 0:
            currentNode = Q.pop(0)
            for child in currentNode.children:
                Q.append(child)
            numberOfChildren -= 1
        Level += 1
    return Level


root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
if not root:
    print 0
    exit()
LevelOrder(root)
