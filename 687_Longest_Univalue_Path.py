#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/longest-univalue-path/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LUP(root):
    global Max
    if not root:
        return 0
    leftLength = LUP(root.left)
    rightLength = LUP(root.right)
    if root.left and root.left.val == root.val:
        leftLength += 1
    else:
        leftLength = 0
    if root.right and root.right.val == root.val:
        rightLength += 1
    else:
        rightLength = 0

    Max = max(Max, leftLength+rightLength)
    return max(leftLength, rightLength)


root = TreeNode(4)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Max = 0
LUP(root)
print Max
