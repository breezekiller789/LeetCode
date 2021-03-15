#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/binary-tree-inorder-traversal/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    # print root.val
    Ans.append(root.val)
    Inorder(root.right)


Ans = []
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
Inorder(root)
print Ans
