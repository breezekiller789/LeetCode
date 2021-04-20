#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/closest-binary-search-tree-value-ii/


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
        prev_Min = Min_Diff[0]
        prev_Min_Node = Min_Diff[1]
        Min_Diff = Diff, root.val, prev_Min, prev_Min_Node
    elif Diff < Min_Diff[2]:
        prev_Min = Min_Diff[0]
        prev_Min_Node = Min_Diff[1]
        Min_Diff = prev_Min, prev_Min_Node, Diff, root.val
    print root.val
    Inorder(root.left)
    Inorder(root.right)


Min_Diff = [float("inf"), 0, float("inf"), 0]
target = 3.714286
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

Inorder(root)
print Min_Diff
