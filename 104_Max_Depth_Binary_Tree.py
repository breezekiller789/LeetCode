#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# 用遞迴解，資結範例


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


def Depth(root):
    if not root:
        return 0
    else:
        L_Height = Depth(root.left)
        R_Height = Depth(root.right)
        return max(L_Height, R_Height) + 1


# 生測資
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print Depth(root)
