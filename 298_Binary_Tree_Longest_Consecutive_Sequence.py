#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

# 1. Preorder Traversal
# 2. each iteration, pass in root, previous, Count, maxLengthSoFar and
# return maxLengthSoFar cuz we need to keep track of it.

# =========Code=========


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root, previous, Count, maxLengthSoFar):
    if not root:
        return maxLengthSoFar
    # if consecutive, add count, and check
    if previous+1 == root.val:
        Count += 1
        maxLengthSoFar = max(maxLengthSoFar, Count)
    # not consecutive, set count to 1
    else:
        Count = 1
    maxLengthSoFar = Preorder(
        root.left,
        root.val,
        Count,
        maxLengthSoFar,
    )
    maxLengthSoFar = Preorder(
        root.right,
        root.val,
        Count,
        maxLengthSoFar,
    )
    return maxLengthSoFar


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print Preorder(root, root.val, 0, 0)
