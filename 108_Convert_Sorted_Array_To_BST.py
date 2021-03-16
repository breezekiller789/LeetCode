#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class BST(object):
#     def __init__(self):
#         self.root = None

def BST_Insert(root, val):
    if not root:
        new_Node = TreeNode(val)
        return new_Node
    if root.val > val:
        root.left = BST_Insert(root.left, val)
    elif root.val < val:
        root.right = BST_Insert(root.right, val)
    return root


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


# nums = [-10, -3, 0, 5, 9]
nums = [0, 1, 2, 3, 4, 5]
length = len(nums)
num_left = nums[:length/2]
num_right = (nums[length/2+1:])[::-1]
# print num_left, num_right
# exit()
root = TreeNode(nums[len(nums)/2])
while num_left:
    root = BST_Insert(root, num_left.pop())
while num_right:
    root = BST_Insert(root, num_right.pop())
Inorder(root)
