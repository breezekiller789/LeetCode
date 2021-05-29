#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# 用遞迴解


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def ReverseInorder(root, Sum):
    if not root:
        return Sum
    Sum = ReverseInorder(root.right, Sum)
    Sum += root.val
    root.val = Sum
    Sum = ReverseInorder(root.left, Sum)
    return Sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
ReverseInorder(root, 0)
