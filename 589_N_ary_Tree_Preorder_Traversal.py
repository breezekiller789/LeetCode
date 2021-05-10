#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Implement by using queue


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.children = []


def Preorder(root, ret):
    if not root:
        return
    ret.append(root.val)
    for child in root.children:
        Preorder(child, ret)


root = TreeNode(1)
root.children.append(TreeNode(3))
root.children.append(TreeNode(2))
root.children.append(TreeNode(4))
root.children[0].children.append(TreeNode(5))
root.children[0].children.append(TreeNode(6))
ret = []
Preorder(root, ret)
print ret
