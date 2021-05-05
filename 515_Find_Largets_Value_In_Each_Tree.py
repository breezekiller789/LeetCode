#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# 1. Use the concept of n-ary tree level order traversal, each level, we get the
# maximum number, and put it in a list, return the list. Reference Q.429


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    Q = [root]
    Ans = []
    while Q:
        count = len(Q)
        Max = float("-inf")
        while count > 0:
            currentNode = Q[0]
            del Q[0]
            Max = max(Max, currentNode.val)
            if currentNode.left:
                Q.append(currentNode.left)
            if currentNode.right:
                Q.append(currentNode.right)
            count -= 1
        Ans.append(Max)
    return Ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
if not root:
    print []
print LevelOrderTraversal(root)
