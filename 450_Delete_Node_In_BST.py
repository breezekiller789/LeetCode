#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/delete-node-in-a-bst/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root):
    if not root:
        return
    print root.val
    Preorder(root.left)
    Preorder(root.right)


# Go left one node, and then go right all the way down
def SearchForClosestNode(root, prev, STATE):
    grandpa = prev      # Grandpa
    prev = root         # Parent
    tmp = root.left     # Grand Child

    # if root is leaf, change pointers to None and return directly
    if not root.left and not root.right:
        if STATE == "Left":
            grandpa.left = None
        elif STATE == "Right":
            grandpa.right = None
        return None
    # Go left, and encounter NULL directly
    if not tmp:
        return prev.right
    # Go all the way down to the right
    goRightOnce = False
    while tmp.right:
        goRightOnce = True
        prev = tmp
        tmp = tmp.right
    if not goRightOnce:    # Enter this if we didn't even go right
        return tmp
    else:                  # We have gone right at least once
        prev.right = tmp.left
        tmp.left = None
        tmp.right = None
        return tmp


def BST_Delete(root, target, prev, STATE):
    if root.val == target:
        closestNode = SearchForClosestNode(root, prev, STATE)
        if not closestNode:     # the deleted node is a leaf, return directly
            return
        if STATE == "Left":                 # remove left child
            if closestNode != root.right:
                closestNode.right = root.right
            if closestNode != root.left:
                closestNode.left = root.left
            prev.left = closestNode         # insert the chosen node
            return
        elif STATE == "Right":              # remove right child
            if closestNode != root.right:
                closestNode.right = root.right
            if closestNode != root.left:
                closestNode.left = root.left
            prev.right = closestNode        # insert the chosen node
            return
        else:                               # remove root
            if root.left != closestNode:    # Added this to cover left skew tree
                closestNode.left = root.left
            if root.right != closestNode:   # cover right skew tree
                closestNode.right = root.right
            root = closestNode
            return root
    if root.val < target:
        BST_Delete(root.right, target, root, "Right")
    if root.val > target:
        BST_Delete(root.left, target, root, "Left")
    return root


root = TreeNode(3)
root.left = TreeNode(1)
# root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right = TreeNode(7)
# root.right.left = TreeNode(6)
# root.right.left.left = TreeNode(5)
# root.right.right = TreeNode(8)
# root.right.right.right = TreeNode(9)
target = 3
# Preorder(root)
# print "==========="
Preorder(BST_Delete(root, target, root, None))
