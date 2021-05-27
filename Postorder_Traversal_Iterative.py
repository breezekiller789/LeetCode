#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Postorder(root):
    # LRD :
    #   - Visit Left node
    #   - Visite Right node
    #   - Visit current node's Data
    stack = []
    currentNode = root
    while True:
        # Visit Left Node First
        if currentNode:
            stack.append(currentNode)
            currentNode = currentNode.left
        elif stack:
            # We have gone to the very left
            # - Visit right node
            oldcurrentNode = stack.pop()
            currentNode = oldcurrentNode.right
            print oldcurrentNode.val
        else:
            break


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Postorder(root)
