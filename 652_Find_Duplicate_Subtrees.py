#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-duplicate-subtrees/


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Equal(root1, root2):
    if not root1 and not root2:
        return True
    elif root1 and root2:
        if root1.val == root2.val and Equal(root1.left, root2.left):
            return Equal(root1.right, root2.right)


def LevelOrderTravesal(root, Nodes):
    Q = [root]
    while Q:
        currentNode = Q.pop(0)
        Nodes.append(currentNode)
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)


def Preorder(root, List):
    if not root:
        return
    List.append(root.val)
    Preorder(root.left, List)
    Preorder(root.right, List)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)
Nodes = []
LevelOrderTravesal(root, Nodes)
Ans = set()
for idx, node in enumerate(Nodes):
    for jdx in range(idx+1, len(Nodes)):
        if Equal(node, Nodes[jdx]):
            if Nodes[jdx] not in Ans and node not in Ans:
                Ans.add(Nodes[jdx])

FinalAnswer = []
TraversedList = []
for node in Ans:
    List = []
    Preorder(node, List)
    if List not in TraversedList:
        TraversedList.append(List)
        FinalAnswer.append(node)
