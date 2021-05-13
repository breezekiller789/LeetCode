#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/trim-a-binary-search-tree/

# This tree recursion question is so interesting...


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Post order
def Trim(root, low, high):
    if not root:
        return
    root.left = Trim(root.left, low, high)
    root.right = Trim(root.right, low, high)
    if root.val < low:
        return root.right
    if root.val > high:
        return root.left
    return root


root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
low = 1
high = 4
Trim(root, low, high)
