#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/insert-into-a-binary-search-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Insert(root, val):
    if not root:
        newNode = TreeNode(val)
        return newNode
    if root.val > val:
        root.left = Insert(root.left, val)
    if root.val < val:
        root.right = Insert(root.right, val)
    return root


def Level(root):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        print currentNode.val
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
val = 5
Insert(root, val)
Level(root)
