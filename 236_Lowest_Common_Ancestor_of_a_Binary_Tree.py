#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Preorder + Level order traversal
# 先讓他走到最底，然後我從最底層開始找，每一個節點我就用level order下去擴散找，
# 如果目標都在我level order traversal底下找得到，那就代表我現在的root就是lowest
# common ancestor了。


class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def Find(root, p, q):
    Q = [root]
    Foundp = None
    Foundq = None
    while Q:
        currentNode = Q.pop()
        if currentNode.val == p:
            Foundp = True
        elif currentNode.val == q:
            Foundq = True
        if Foundp and Foundq:
            return True
        if currentNode.left:
            Q.append(currentNode.left)
        if currentNode.right:
            Q.append(currentNode.right)
    return False


def Preorder(root, p, q):
    if not root:
        return

    # Go all the way left
    ret = Preorder(root.left, p, q)
    # 這邊這個if-statement就是在接我從下面傳回來的結果。
    if ret:
        return ret

    # Go all the way right
    ret = Preorder(root.right, p, q)
    # 這邊這個if-statement就是在接我從下面傳回來的結果。
    if ret:
        return ret

    # 如果Find回傳true，代表p, q都在我這個root底下，可以直接回傳。
    if Find(root, p, q):
        return root
    else:
        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
p = 4
q = 7
print Preorder(root, p, q).val
