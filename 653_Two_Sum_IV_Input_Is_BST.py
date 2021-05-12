#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Since input is a BST, so if we inorder traverse the tree, we will get a sorted
# array, and that being said, we can use two pointers to solve the two sum
# problem directly.


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root, nodes):
    if not root:
        return
    # LDR   L->left, D->Data, R->right
    Inorder(root.left, nodes)
    nodes.append(root.val)
    Inorder(root.right, nodes)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

target = 6
nodes = []
Inorder(root, nodes)    # nodes will be a sorted array

# Two pointers approach
low = 0
high = len(nodes)-1
while low < high:
    val = nodes[low] + nodes[high]
    if val < target:
        low += 1
    elif val > target:
        high -= 1
    else:
        print True
        exit()
print False
