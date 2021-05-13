#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LevelOrderTraversal(root, List):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        List.append(currentNode.val)
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)


List = []
LevelOrderTraversal(root, List)
Min = min(List)     # Get the actual minimum
finalMin = float("inf")
for num in List:
    # We wanna get the second minimum, so we have to skip the actual minimum
    if num == Min:
        continue
    finalMin = min(finalMin, num)

# Enter this second minimum doesn't exist
if finalMin == float("inf"):
    print -1
    exit()
print finalMin
