#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/path-sum-iii/

# 1. Level order traversal and preorder traversal

# ========Code=========


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LevelOrder(root):
    Q = [root]
    while Q:
        currentNode = Q[0]
        del Q[0]
        Preorder(currentNode, 0)
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)


def Preorder(root, Sum):
    global targetSum
    global total
    if not root:
        return
    Sum += root.val
    if Sum == targetSum:
        total += 1
    if not root.left and not root.right:
        # Current root is leaf
        return
    Preorder(root.left, Sum)
    Preorder(root.right, Sum)
    Sum -= root.val


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right.right = TreeNode(11)
targetSum = 8
total = 0
LevelOrder(root)
print total
