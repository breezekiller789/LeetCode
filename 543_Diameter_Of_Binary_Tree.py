#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/diameter-of-binary-tree/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# return the height of this tree
def Height(root):
    if not root:
        return -1   # Since if want the root has height 0, so return -1
    leftHeight = Height(root.left)
    rightHeight = Height(root.right)
    return max(leftHeight, rightHeight)+1


def LevelOrderTraversal(root):
    Q = [root]
    Max = float("-inf")
    while Q:
        currentNode = Q.pop(0)
        leftHeight = Height(currentNode.left)   # Get the height of left subtree
        rightHeight = Height(currentNode.right)   # Height of right subtree
        Max = max(Max, leftHeight+rightHeight+2)  # Update the Max length
        if currentNode.left:        # Level order traverse
            Q.append(currentNode.left)
        if currentNode.right:       # Level order traverse
            Q.append(currentNode.right)
    return Max


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
print LevelOrderTraversal(root)
