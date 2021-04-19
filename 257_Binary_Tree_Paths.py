#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-paths/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root, String, Paths):
    if not root:
        return
    if not root.left and not root.right:
        String.append(root.val)
        Paths.append(String[:])
        String.pop()
        return
    String.append(root.val)
    Inorder(root.left, String, Paths)
    Inorder(root.right, String, Paths)
    String.pop()


String = []
Paths = []
Ans = []
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.right.left = TreeNode(4)
root.left.right = TreeNode(5)
Inorder(root, String, Paths)

for item in Paths:
    string = ""
    for element in item:
        string += str(element)+"->"
    Ans.append(string[:-2])
print Ans
