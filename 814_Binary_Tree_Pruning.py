#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-pruning/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ahah = 0

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.ahah = 0

        def RecursivePrune(root):
            if not root:
                return True
            leftNoOne = RecursivePrune(root.left)
            rightNoOne = RecursivePrune(root.right)
            # 如果左子樹都是0，就刪掉它
            if leftNoOne:
                root.left = None
            # 右子樹都是0，刪掉它
            if rightNoOne:
                root.right = None
            # 回傳是否左右子樹都是零，還有root是不是也是0
            return leftNoOne and rightNoOne and root.val == 0
        RecursivePrune(root)
        if not root.left and not root.right and root.val == 0:
            return None
        return root
