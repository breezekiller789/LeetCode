#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sum-of-left-leaves/

# 1. use preorder traversal
# 2. we have to pass in STATE, which indicates direction of parent, "Left" means
# this child is the left node of parent node, and also pass in Sum

# ========Code=========


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root, STATE, Sum):
    if not root:
        return Sum
    if not root.left and not root.right and STATE == "Left":
        Sum += root.val
        return Sum
    Sum = Preorder(root.left, "Left", Sum)
    Sum = Preorder(root.right, "Right", Sum)
    return Sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print Preorder(root, "None", 0)
