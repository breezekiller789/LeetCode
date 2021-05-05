#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-bottom-left-tree-value/

# Basically it's just like how compilers work, pass in attributes and return
# result, using preorder traversal. Pass in depth, maxDepth, return value and
# root.


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root, depth, maxDepth, ret):
    if not root:
        return maxDepth, ret

    # Enter this if-statement if current root is leaf and also current level is
    # deeper than the maximum depth.
    if depth > maxDepth and not root.left and not root.right:
        maxDepth = depth
        return maxDepth, root.val

    maxDepth, ret = Preorder(root.left, depth+1, maxDepth, ret)
    maxDepth, ret = Preorder(root.right, depth+1, maxDepth, ret)
    return maxDepth, ret


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
depth = 0
print Preorder(root, depth, 0, 0)
