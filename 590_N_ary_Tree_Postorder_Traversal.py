#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/n-ary-tree-postorder-traversal/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.children = []


def Postorder(root, ret):
    if not root:
        return
    while root.children:
        child = root.children.pop(0)
        Postorder(child, ret)
    ret.append(root.val)


root = TreeNode(1)
root.children.append(TreeNode(3))
root.children.append(TreeNode(2))
root.children.append(TreeNode(4))
root.children[0].children.append(TreeNode(5))
root.children[0].children.append(TreeNode(6))
ret = []
Postorder(root, ret)
print ret
