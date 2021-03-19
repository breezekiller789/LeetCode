#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BST_Min(root):
    if not root.left:
        return root.val
    return BST_Min(root.left)


root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

print BST_Min(root)
