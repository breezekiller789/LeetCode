#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=-tNMxwWSN_M&t=705s


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def RecursiveSum(root, depth):
    if not root:
        return 0
    leftSum = RecursiveSum(root.left, depth+1)
    rightSum = RecursiveSum(root.right, depth+1)
    return leftSum + rightSum + depth


def LevelOrder(root):
    Q = [root]
    Sum = 0
    while Q:    # O(n)
        currentNode = Q.pop()
        Sum += RecursiveSum(currentNode, 0)  # O(n)
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)
    # Time: O(n^2)
    return Sum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
Sum = 0
#             1
#           /  \
#          2    3
#         / \  / \
#        4   5 6  7
#       / \
#      8   9
print LevelOrder(root)
# print RecursiveSum(root, 0)
