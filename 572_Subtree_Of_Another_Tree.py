#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subtree-of-another-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Equal(root, root1):
    if not root and not root1:
        return True
    if root and root1:
        if root.val == root1.val:
            if Equal(root.left, root1.left):
                return Equal(root.right, root1.right)
    return False


def LevelOrderTraversal(root, root1):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        if Equal(currentNode, root1):
            return True
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)
    return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
# root1.right.right = TreeNode(7)
print LevelOrderTraversal(root, root1)
# print Equal(root, root1)
