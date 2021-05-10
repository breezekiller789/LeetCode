#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/merge-two-binary-trees/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        print currentNode.val
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)


def MergeBinaryTree(root1, root2):
    if not root1 and not root2:
        return
    root1Value = 0
    root2Value = 0
    if root1:
        root1Value = root1.val
    if root2:
        root2Value = root2.val
    newRoot = TreeNode(root1Value+root2Value)
    if root1 and root2:
        newRoot.left = MergeBinaryTree(root1.left, root2.left)
        newRoot.right = MergeBinaryTree(root1.right, root2.right)
    elif root1 and not root2:
        newRoot.left = MergeBinaryTree(root1.left, None)
        newRoot.right = MergeBinaryTree(root1.right, None)
    elif not root1 and root2:
        newRoot.left = MergeBinaryTree(None, root2.left)
        newRoot.right = MergeBinaryTree(None, root2.right)
    return newRoot


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print root.val
    Inorder(root.right)


def Preorder(root):
    if not root:
        return
    print root.val
    Preorder(root.left)
    Preorder(root.right)


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

root = MergeBinaryTree(root1, root2)
LevelOrderTraversal(root)
