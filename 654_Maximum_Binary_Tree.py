#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/maximum-binary-tree/

# I solved this using recursion, a very simple recursion concept


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def MaximumBinaryTree(nums):
    if not nums:
        return
    rootvalue = max(nums)           # Get the max value as root value
    root = TreeNode(rootvalue)      # Get a Tree object
    index = nums.index(rootvalue)   # Get the index of max value to split array
    leftList = nums[0:index]        # Left side of array, not including root
    rightList = nums[index+1:]      # Right side of array, not including root

    root.left = MaximumBinaryTree(leftList)     # Recursively get left node
    root.right = MaximumBinaryTree(rightList)   # Recursively get right node
    return root


# this is just for me to see if result is correct
def LevelOrderTraversal(root):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        print currentNode.val
        if currentNode.left:
            # current node has left children
            Q.append(currentNode.left)
        if currentNode.right:
            # current node has right children
            Q.append(currentNode.right)


nums = [3, 2, 1, 6, 0, 5]
# nums = [3, 2, 1]
root = MaximumBinaryTree(nums)
LevelOrderTraversal(root)
