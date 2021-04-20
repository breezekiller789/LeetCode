#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/closest-binary-search-tree-value/

# 1. Inorder traversal, check every value, substract them, and get the smallest

# ==========Code=========


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root):
    global Min_Diff
    if not root:
        return
    Diff = abs(root.val - target)
    if Diff < Min_Diff[0]:
        Min_Diff = Diff, root.val
    print root.val
    Inorder(root.left)
    Inorder(root.right)


Min_Diff = [float("inf"), 0]
target = 3.714286
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

Inorder(root)
print Min_Diff
