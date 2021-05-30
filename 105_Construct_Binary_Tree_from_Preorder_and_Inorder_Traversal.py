#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# 這一定要用遞迴，用遞迴解比較直覺


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
# preorder = [-1]
# inorder = [-1]


def RecursiveConstruct(preorder, inorder):
    if not preorder or not inorder:
        return
    root = TreeNode(preorder[0])
    rootIndex = inorder.index(root.val)
    del preorder[0]
    root.left = RecursiveConstruct(preorder, inorder[:rootIndex])
    root.right = RecursiveConstruct(preorder, inorder[rootIndex+1:])
    return root


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


root = RecursiveConstruct(preorder, inorder)
Inorder(root)
