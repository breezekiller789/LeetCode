#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/binary-tree-preorder-traversal/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.right = None
        self.left = None


def Preorder(root):
    if not root:
        return
    print root.val
    Preorder(root.left)
    Preorder(root.right)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

Preorder(root)
