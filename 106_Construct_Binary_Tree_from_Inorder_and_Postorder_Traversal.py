#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# 跟105很像，只是這是postorder，差別在於我們組成的時候，要右邊先接再換左邊。


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]
# preorder = [-1]
# inorder = [-1]


def RecursiveConstruct(postorder, inorder):
    if not postorder or not inorder:
        return
    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(root.val)
    del postorder[-1]
    root.right = RecursiveConstruct(postorder, inorder[rootIndex+1:])
    root.left = RecursiveConstruct(postorder, inorder[:rootIndex])
    return root


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


root = RecursiveConstruct(postorder, inorder)
Inorder(root)
