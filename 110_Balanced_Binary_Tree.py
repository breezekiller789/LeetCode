#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/balanced-binary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def IsBalanced(root):
    if not root:
        return 0, True
    leftHeight, leftret = IsBalanced(root.left)
    rightHeight, rightret = IsBalanced(root.right)
    return max(leftHeight, rightHeight) + 1, abs(leftHeight-rightHeight) <= 1\
        and leftret and rightret


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print IsBalanced(root)[1]
