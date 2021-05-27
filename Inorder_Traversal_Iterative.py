#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Inorder(root):
    stack = []
    currentNode = root
    while True:
        if currentNode:
            stack.append(currentNode)
            currentNode = currentNode.left
        elif stack:
            # CurrentNode is None, visit parent node, just pop from stack, and
            # then visit right node
            currentNode = stack.pop()   # Pop from stack, visit parent
            print currentNode.val       # visit
            currentNode = currentNode.right  # visit right nodes
        # if currentNode is None and stack is also None, end it
        else:
            break


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Inorder(root)
