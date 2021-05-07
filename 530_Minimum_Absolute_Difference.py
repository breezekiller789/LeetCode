#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root, Nodes):
    if not root:
        return
    Inorder(root.left, Nodes)
    Nodes.append(root.val)
    Inorder(root.right, Nodes)


root = TreeNode(1)
root.left = TreeNode(100)
root.right = TreeNode(50)
root.left.left = TreeNode(20)
root.left.right = TreeNode(23)
root.right.left = TreeNode(42)
root.right.right = TreeNode(45)
Nodes = []
Inorder(root, Nodes)
# print Nodes
minDiff = float("inf")
for idx, node in enumerate(Nodes[:-1]):
    minDiff = min(minDiff, abs(node-Nodes[idx+1]))
print minDiff
