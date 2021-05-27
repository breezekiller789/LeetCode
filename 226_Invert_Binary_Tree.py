#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/invert-binary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


class Solution(object):
    def __init__(self):
        self.haha = 0

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.haha = 0

        def Invert(root):
            if not root:
                return
            leftSubTree = Invert(root.left)     # Invert your left and right!
            rightSubTree = Invert(root.right)   # Invert you left and right!
            root.left = rightSubTree
            root.right = leftSubTree
            return root
        Invert(root)
        return root


obj = Solution()
obj.invertTree(root)
