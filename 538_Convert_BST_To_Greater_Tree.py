#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/convert-bst-to-greater-tree/

# This question is really similar to how compilers work!!


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Traverse(root, Sum):
    if not root:
        return Sum
    # If root is leaf, update its value and then return the Sum
    if not root.left and not root.right:
        Sum += root.val
        root.val = Sum
        return Sum
    Sum = Traverse(root.right, Sum)     # Go right
    Sum += root.val                     # Update Sum
    root.val = Sum                      # Update root value
    Sum = Traverse(root.left, Sum)      # Go left
    return Sum


def LevelOrderTraversal(root):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        print currentNode.val
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
Traverse(root, 0)
LevelOrderTraversal(root)
