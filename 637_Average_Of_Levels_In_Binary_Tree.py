#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/average-of-levels-in-binary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    Q = [root]
    ret = []
    while Q:
        childCount = len(Q)
        count = 0
        Sum = 0
        while count < childCount:
            currentNode = Q.pop(0)
            Sum += currentNode.val
            if currentNode.left:
                Q.append(currentNode.left)
            if currentNode.right:
                Q.append(currentNode.right)
            count += 1
        ret.append(float(Sum) / float(childCount))
    return ret


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print LevelOrderTraversal(root)
