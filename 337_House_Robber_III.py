#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/tag/dynamic-programming/

# Recursion + memoization


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def RecursiveRobber(root, alreadyChecked):

    if not root:
        return 0

    if root in alreadyChecked:
        return alreadyChecked[root]

    # Don't pick this node so rob next level
    dontPickedLeft = RecursiveRobber(root.left, alreadyChecked)
    dontPickedRight = RecursiveRobber(root.right, alreadyChecked)

    pickedLeftLeft = 0
    pickedLeftRight = 0
    pickedRightLeft = 0
    pickedRightRight = 0

    # Don't pick this node so rob the next 2 level
    if root.left:
        pickedLeftLeft = RecursiveRobber(root.left.left, alreadyChecked)
        pickedLeftRight = RecursiveRobber(root.left.right, alreadyChecked)

    # Don't pick this node so rob the next 2 level
    if root.right:
        pickedRightLeft = RecursiveRobber(root.right.left, alreadyChecked)
        pickedRightRight = RecursiveRobber(root.right.right, alreadyChecked)

    # Memorize this node
    alreadyChecked[root] = max(dontPickedLeft+dontPickedRight,
                               pickedLeftLeft + pickedLeftRight +
                               pickedRightLeft + pickedRightRight + root.val)
    return alreadyChecked[root]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
#             1
#           /  \
#          2    3
#         / \  / \
#        4   5 6  7
alreadyChecked = dict()
print RecursiveRobber(root, alreadyChecked)
