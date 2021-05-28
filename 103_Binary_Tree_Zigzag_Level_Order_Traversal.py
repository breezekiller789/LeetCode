#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.haha = 0

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.haha = 0

        def LevelOrder(root, result):
            Q = [root]
            Level = 0
            while Q:
                childCount = len(Q)
                newList = []
                while childCount > 0:
                    currentNode = Q.pop(0)
                    newList.append(currentNode.val)
                    if currentNode.left:
                        Q.append(currentNode.left)
                    if currentNode.right:
                        Q.append(currentNode.right)
                    childCount -= 1
                if Level % 2 == 0:
                    result.append(newList)
                else:
                    result.append(newList[::-1])
                Level += 1
        if not root:
            return []
        result = []
        LevelOrder(root, result)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
obj = Solution()
print obj.zigzagLevelOrder(root)
