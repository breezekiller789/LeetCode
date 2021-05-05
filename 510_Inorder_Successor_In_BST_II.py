#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/inorder-successor-in-bst-ii/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# 1. If node has right child, then successor must be in somewhere down the tree,
# actually it is go right and then go left till the node has no left node
# 2. If node has no right child, then we have to go up, until we have the parent
# that it's left node is our lower parent, if we go all the up til the root,
# then return null
node = TreeNode(0)
if node.right:
    tmp = node.right    # Go right one step
    while tmp.left:     # Go all the way down
        tmp = tmp.left
    return tmp
else:
    # Go up
    tmp = node
    while tmp.parent:
        if tmp.parent.left == tmp:
            break
        tmp = tmp.parent
    if not tmp.parent:
        return None
    return tmp.parent



# My Initial thoughts, it was very slow
# def Inorder(root, Array):
#     if not root:
#         return
#     Inorder(root.left, Array)
#     Array.append(root)
#     Inorder(root.right, Array)


# node = TreeNode(0)
# tmp = node
# while tmp.parent:
#     tmp = tmp.parent
# Array = []
# Inorder(tmp, Array)
# idx = Array.index(node)
# if idx == len(Array)-1:
#     print None
# else:
#     print Array[idx+1]
