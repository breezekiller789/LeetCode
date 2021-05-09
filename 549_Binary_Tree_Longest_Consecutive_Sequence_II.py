#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root, parent, maxLength):
    # Empty root
    if not root:
        return 0, 0, maxLength

    # This node is leaf
    if not root.left and not root.right:
        return 0, 0, maxLength     # Increase, Decrease

    # Go left
    leftIncrease, leftDecrease, maxLength = Preorder(root.left, root, maxLength)

    # Go right
    rightIncrease, rightDecrease, maxLength = Preorder(
        root.right, root, maxLength)

    maxLength = max(maxLength, leftIncrease+rightDecrease+1,
                    leftDecrease+rightIncrease+1)

    # It's decreasing
    if root.val == parent.val+1:
        return 0, max(leftDecrease, rightDecrease)+1, maxLength
    if root.val == parent.val-1:
        return max(leftIncrease, rightIncrease)+1, 0, maxLength
    return 0, 0, maxLength


root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)
print Preorder(root, root, 0)
