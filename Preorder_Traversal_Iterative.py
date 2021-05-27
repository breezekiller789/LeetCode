#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Preorder(root):
    # DLR
    stack = []
    currentNode = root
    while True:
        if currentNode:
            print currentNode.val
            stack.append(currentNode)
            currentNode = currentNode.left
        elif stack:
            # currentNode is None -> don't have any left nodes to visit, visit
            # right nodes instead
            currentNode = stack.pop()
            currentNode = currentNode.right
        else:
            break


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Preorder(root)
