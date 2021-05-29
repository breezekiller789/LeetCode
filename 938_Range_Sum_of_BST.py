#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/range-sum-of-bst/

# Tree traversal


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.haha = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.haha = 0

        def Inorder(root, low, high):
            global Sum
            if not root:
                return
            Inorder(root.left, low, high)
            if root.val >= low and root.val <= high:
                Sum += root.val
            Inorder(root.right, low, high)
        global Sum
        Sum = 0
        Inorder(root, low, high)
        return Sum


Sum = 0
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
