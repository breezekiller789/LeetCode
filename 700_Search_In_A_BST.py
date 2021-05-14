#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-in-a-binary-search-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root, val):
    if not root:
        return
    if root.val > val:
        return Inorder(root.left, val)
    elif root.val < val:
        return Inorder(root.right, val)
    else:
        return root


def Preorder(root):
    if not root:
        return
    print root.val
    Preorder(root.left)
    Preorder(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
val = 2
root = Inorder(root, val)
Preorder(root)
