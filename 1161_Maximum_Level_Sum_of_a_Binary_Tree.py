#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Level order traversal


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.haha = 0

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.haha = 0

        def LevelOrder(root):
            Q = [root]
            Level = 1
            Max = [float("-inf"), Level]
            while Q:
                childCount = len(Q)
                Sum = 0
                while childCount > 0:
                    currentNode = Q.pop(0)
                    Sum += currentNode.val
                    if currentNode.left:
                        Q.append(currentNode.left)
                    if currentNode.right:
                        Q.append(currentNode.right)
                    childCount -= 1
                if Sum > Max[0]:
                    Max = [Sum, Level]
                Level += 1
            return Max[1]
        return LevelOrder(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

obj = Solution()
obj.maxLevelSum(root)
